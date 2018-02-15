from rest_framework import mixins
from rest_framework import viewsets
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.authentication import SessionAuthentication
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

from .serializers import UserVoteSerializer
from .models import UserVote


class UserVoteViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet,
                      mixins.CreateModelMixin, mixins.DestroyModelMixin):

    """
    用户赞同 / 反对
    """

    serializer_class = UserVoteSerializer
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter,)
    filter_fields = ('vote_type',)
    search_fields = ('answer__question__id',)
    lookup_field = "answer"

    def get_queryset(self):
        return UserVote.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        instance = serializer.save()
        vote_type = instance.vote_type
        answer = instance.answer
        if vote_type == 'up':
            answer.up_vote()
        if vote_type == 'down':
            answer.down_vote()

    def perform_destroy(self, instance):
        vote_type = instance.vote_type
        answer = instance.answer
        if vote_type == 'up':
            answer.down_vote()
        if vote_type == 'down':
            answer.up_vote()
        instance.delete()
