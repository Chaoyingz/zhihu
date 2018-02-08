import re
from datetime import datetime, timedelta

from rest_framework import serializers
from rest_framework.reverse import reverse

from django.contrib.auth import get_user_model
from .models import VerifyCode

User = get_user_model()


class UserProfileSerializers(serializers.ModelSerializer):

    """
    UserProfile Serializer
    """

    password = serializers.CharField(
        style={'input_type': 'password'}, label="密码", write_only=True,
    )
    links = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ("username", "gender", "email", "password", "views", "links")

    def get_links(self, obj):
        request = self.context['request']
        return reverse('user-detail', kwargs={'pk': obj.pk},
                       request=request)


class SmsSerializers(serializers.Serializer):

    """
    验证码序列化
    """

    mobile = serializers.CharField(max_length=11)

    def validate_mobile(self, mobile):

        # 验证手机号码是否合法
        REGEX_MOBILE = "^1[358]\d{9}$|^147\d{8}$|^176\d{8}$"
        if not re.match(REGEX_MOBILE, mobile):
            raise serializers.ValidationError("请输入正确的手机号")

        # 手机号是否注册
        if User.objects.filter(mobile=mobile).count():
            raise serializers.ValidationError("您输入的手机号已注册,请登陆")

        # 验证发送频率
        one_mintes_ago = datetime.now() - timedelta(hours=0, minutes=1, seconds=0)
        if VerifyCode.objects.filter(created__gt=one_mintes_ago, mobile=mobile):
            raise serializers.ValidationError("验证频率过高，请一分钟后重试")

        return mobile
