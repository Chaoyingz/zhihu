from rest_framework import serializers

from .models import UserVote


class UserVoteSerializer(serializers.ModelSerializer):

    """
    User Vote Serializer
    """

    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = UserVote
        fields = ('user', 'answer', 'vote_type')
