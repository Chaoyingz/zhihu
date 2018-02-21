from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.authentication import SessionAuthentication
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

from .serializers import AnswerSerializer, TopicSerializer, QuestionSerializer
from .models import Answer, Topic, Question


class BasePagination(PageNumberPagination):

    """
    分页
    """

    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100


class AnswerViewset(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet,
                    mixins.CreateModelMixin,):

    """
    回答
    """

    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    pagination_class = BasePagination
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)


class TopicViewset(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet,
                   mixins.CreateModelMixin,):

    """
    话题
    """

    queryset = Topic.objects.all()
    serializer_class = TopicSerializer
    pagination_class = BasePagination
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)


class QuestionViewset(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet,
                      mixins.CreateModelMixin,):

    """
    问题
    """

    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    pagination_class = BasePagination
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter,)
    search_fields = ('title',)
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        # 统计文章阅读量
        instance.increase_views()
        return Response(serializer.data)
