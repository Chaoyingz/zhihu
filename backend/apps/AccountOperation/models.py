from datetime import datetime

from django.db import models
from django.contrib.auth import get_user_model

from Question.models import Answer

User = get_user_model()


class UserVote(models.Model):

    """
    用户投票
    """

    user = models.ForeignKey(User, verbose_name="用户", related_name='vote', on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, verbose_name="回答", related_name='vote_operation',
                               on_delete=models.CASCADE)
    created = models.DateTimeField(default=datetime.now, verbose_name="添加时间")
    vote_type = models.CharField(max_length=10, choices=(('up', "支持"), ('down', "反对")))

    class Meta:
        unique_together = ('user', 'answer')
        verbose_name = "用户赞同反对"
        verbose_name_plural = verbose_name
