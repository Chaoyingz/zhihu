from django.db import models
from django.contrib.auth.models import AbstractUser


class UserProfile(AbstractUser):

    """
    用户资料模型
    """

    views = models.PositiveIntegerField(default=0, verbose_name="浏览次数")
    desc = models.CharField(max_length=100, verbose_name="描述", blank=True)
    gender = models.CharField(max_length=6, choices=(('male', u"男"),
                             ('female', "女"), ('null', "未知")), default='null',
                             verbose_name="性别")

    class Meta:
        verbose_name = "用户"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username
