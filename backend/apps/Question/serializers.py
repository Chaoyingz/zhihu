from rest_framework import serializers
from rest_framework.reverse import reverse

from .models import Answer, Topic, Question


class AnswerSerializer(serializers.ModelSerializer):

    """
    Answer Serializer
    """

    question = serializers.CharField(source='question.title')
    question_id = serializers.CharField(source='question.id')
    topic = serializers.CharField(source='question.topic')
    author = serializers.CharField(source='author.username')
    author_desc = serializers.CharField(source='author.desc')
    links = serializers.SerializerMethodField()

    class Meta:
        model = Answer
        fields = '__all__'

    def get_links(self, obj):
        request = self.context['request']
        return reverse('answer-detail', kwargs={'pk': obj.pk},
                       request=request)


class TopicSerializer(serializers.ModelSerializer):

    """
    Topic Serializer
    """

    class Meta:
        model = Topic
        fields = '__all__'


class QuestionSerializer(serializers.ModelSerializer):

    """
    Question Serializer
    """

    answers = AnswerSerializer(many=True, read_only=True)
    answers_count = serializers.SerializerMethodField()
    topic = serializers.CharField(source='topic.name', default='',)
    author = serializers.CharField(source='author.username')
    links = serializers.SerializerMethodField()

    class Meta:
        model = Question
        fields = '__all__'

    def get_links(self, obj):
        request = self.context['request']
        return reverse('question-detail', kwargs={'pk': obj.pk},
                       request=request)

    def get_answers_count(self, obj):
        return obj.answers.count()
