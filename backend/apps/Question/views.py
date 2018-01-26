from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination

from .serializers import AnswerSerializers, TopicSerializers, QuestionSerializers
from .models import Answer, Topic, Question


class BasePagination(PageNumberPagination):

    """
    分页
    """

    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100


class AnswerViewset(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):

    """
    回答
    """

    queryset = Answer.objects.all()
    serializer_class = AnswerSerializers
    pagination_class = BasePagination


class TopicViewset(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):

    """
    话题
    """

    queryset = Topic.objects.all()
    serializer_class = TopicSerializers
    pagination_class = BasePagination


class QuestionViewset(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):

    """
    问题
    """

    queryset = Question.objects.all()
    serializer_class = QuestionSerializers
    pagination_class = BasePagination
