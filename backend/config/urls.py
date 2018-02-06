from django.contrib import admin
from django.conf.urls import include
from django.urls import path, re_path

from rest_framework.routers import DefaultRouter
from rest_framework_jwt.views import obtain_jwt_token

from Question.views import AnswerViewset, TopicViewset, QuestionViewset


router = DefaultRouter()

router.register(r'answers', AnswerViewset, base_name='answer')
router.register(r'topics', TopicViewset, base_name='topic')
router.register(r'questions', QuestionViewset, base_name='question')


urlpatterns = [
    # ADMIN URL
    path('admin/', admin.site.urls),
    # LOGIN URL
    path('api/v1/login/', obtain_jwt_token),
    # API URL
    re_path('api/v1/', include(router.urls)),
]
