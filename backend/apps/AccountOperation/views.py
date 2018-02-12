from rest_framework import mixins
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response

from .serializers import UserVoteSerializer
from .models import UserVote


class UserVoteViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet,
                      mixins.CreateModelMixin, mixins.DestroyModelMixin):

    """
    用户支持 / 反对
    """

    serializer_class = UserVoteSerializer

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
