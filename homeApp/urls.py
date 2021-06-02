from django.urls import path
from . import views

urlpatterns = [
    path('peoples', views.peoplesView),
    path('write-answers/<int:que_id>', views.writeAnsView, name="ans_page"),
    # path('post-question', views.postQueView),

]