from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser


class UserProfile(AbstractUser):

    """
    用户资料模型
    """

    mobile = models.CharField(max_length=11, blank=True, verbose_name="手机号")
    email = models.EmailField(max_length=254, blank=True, verbose_name="邮箱")
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


class VerifyCode(models.Model):

    """
    验证码
    """

    code = models.CharField(max_length=10, verbose_name="验证码")
    mobile = models.CharField(max_length=11, verbose_name="手机号")
    created = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "短信验证码"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.code
