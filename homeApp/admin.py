from django.contrib import admin
from .models import  QuestionsModel, AnswersModel, FollowModel, Followers


# Register your models here.
admin.site.register(QuestionsModel)
admin.site.register(AnswersModel)
admin.site.register(FollowModel)
admin.site.register(Followers)