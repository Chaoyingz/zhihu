from rest_framework import serializers

from .models import UserVote, UserFlowQuestion


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
