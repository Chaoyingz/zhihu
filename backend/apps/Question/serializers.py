from rest_framework import serializers

from .models import Answer, Topic, Question


class AnswerSerializers(serializers.ModelSerializer):

    """
    Answer Serializer
    """

    question = serializers.CharField(source='question.title')
    topic = serializers.CharField(source='question.topic')
    author = serializers.CharField(source='author.username')
    author_desc = serializers.CharField(source='author.desc')

    class Meta:
        model = Answer
        fields = '__all__'


class TopicSerializers(serializers.ModelSerializer):

    """
    Topic Serializer
    """

    class Meta:
        model = Topic
        fields = '__all__'


class QuestionSerializers(serializers.ModelSerializer):

    """
    Question Serializer
    """

    topic = serializers.CharField(source='topic.name')
    author = serializers.CharField(source='author.username')

    class Meta:
        model = Question
        fields = '__all__'
