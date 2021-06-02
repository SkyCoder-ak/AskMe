from django.contrib import admin
from .models import QuestionsModel
from .models import AnswersModel

# Register your models here.
admin.site.register(QuestionsModel)
admin.site.register(AnswersModel)