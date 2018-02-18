from django.contrib import admin
from django.conf.urls import include
from django.urls import path, re_path

from rest_framework.routers import DefaultRouter
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework.authtoken import views

from Question.views import AnswerViewset, TopicViewset, QuestionViewset
from Account.views import UserProfileViewSet, SmsCodeViewSet, UserRegisterViewset
from AccountOperation.views import UserVoteViewSet, UserFlowQuestionViewSet


router = DefaultRouter()

router.register(r'answers', AnswerViewset, base_name='answer')
router.register(r'topics', TopicViewset, base_name='topic')
router.register(r'questions', QuestionViewset, base_name='question')
router.register(r'users', UserProfileViewSet, base_name='user')
router.register(r'codes', SmsCodeViewSet, base_name='code')
router.register(r'register', UserRegisterViewset, base_name='register')
router.register(r'votes', UserVoteViewSet, base_name='vote')
router.register(r'flow_questions', UserFlowQuestionViewSet, base_name='flow_question')


urlpatterns = [
    # ADMIN URL
    path('admin/', admin.site.urls),
    # API LOGIN
    path('api/v1/login/', obtain_jwt_token),
    # API URL
    re_path('api/v1/', include(router.urls)),
    # DRF LOGIN
    path('api-token-auth/', views.obtain_auth_token),
    re_path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
