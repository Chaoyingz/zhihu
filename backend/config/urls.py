from django.contrib import admin
from django.conf.urls import include
from django.urls import path, re_path

from rest_framework.routers import DefaultRouter
from rest_framework_jwt.views import obtain_jwt_token

from Question.views import AnswerViewset, TopicViewset, QuestionViewset
from Account.views import UserProfileViewSet


router = DefaultRouter()

router.register(r'answers', AnswerViewset, base_name='answer')
router.register(r'topics', TopicViewset, base_name='topic')
router.register(r'questions', QuestionViewset, base_name='question')
router.register(r'users', UserProfileViewSet, base_name='user')


urlpatterns = [
    # ADMIN URL
    path('admin/', admin.site.urls),
    # API LOGIN
    path('api/v1/login/', obtain_jwt_token),
    # API URL
    re_path('api/v1/', include(router.urls)),
]
