from django.urls import path
from . import views

urlpatterns = [
    path('peoples', views.peoplesView),
    path('write-answers', views.writeAnsView),

]