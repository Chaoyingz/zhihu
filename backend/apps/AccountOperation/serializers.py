from rest_framework import serializers

from .models import UserVote, UserFlowQuestion, UserFav


class UserVoteSerializer(serializers.ModelSerializer):

    """
    User Vote Serializer
    """

    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    answer_vote = serializers.CharField(source='answer.vote', read_only=True)

    class Meta:
        model = UserVote
        fields = ('user', 'answer', 'vote_type', 'answer_vote')


class UserFlowQuestionSerializer(serializers.ModelSerializer):

    """
    User Flow Question Serializer
    """

    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = UserFlowQuestion
        fields = ('user', 'question')


class UserFavSerializer(serializers.ModelSerializer):

    """
    User Fav Serializer
    """

    question_id = serializers.CharField(source="answer.question.id", read_only=True)
    question_title = serializers.CharField(source="answer.question.title", read_only=True)
    answer_vote = serializers.CharField(source="answer.vote", read_only=True)
    answer_text = serializers.CharField(source="answer.text", read_only=True)
    author_name = serializers.CharField(source="answer.author", read_only=True)
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = UserFav
        fields = "__all__"
