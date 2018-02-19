from datetime import datetime

from django.db import models
from django.contrib.auth import get_user_model

from Question.models import Answer, Question

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


class UserFlowQuestion(models.Model):

    """
    用户关注问题
    """
    user = models.ForeignKey(User, verbose_name="用户", related_name='flow_question',
                             on_delete=models.CASCADE)
    question = models.ForeignKey(Question, verbose_name="问题", related_name='flow_operation',
                                 on_delete=models.CASCADE)
    created = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        unique_together = ('user', 'question')
        verbose_name = "用户关注问题"
        verbose_name_plural = verbose_name


class UserFav(models.Model):

    """
    用户收藏问题
    """

    user = models.ForeignKey(User, verbose_name="用户", related_name='fav',
                             on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, verbose_name="回答", related_name='fav',
                               on_delete=models.CASCADE)
    created = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        unique_together = ('user', 'answer')
        verbose_name = "用户收藏问题"
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.answer.id)
