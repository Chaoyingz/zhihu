from django.contrib import admin

from .models import Topic, Question, Answer


admin.site.register(Topic)
admin.site.register(Question)
admin.site.register(Answer)
