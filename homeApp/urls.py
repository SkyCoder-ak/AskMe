from django.urls import path
from . import views

urlpatterns = [
    path('peoples/<int:p_id>', views.FollowView, name='follow'),
    path('peoples', views.peoplesView, name='peoples_main'),
    path('write-answers/<int:pk>', views.writeAnsView, name="ans_page"),
    path('like-ans/<int:pk>', views.LikeView, name="like_ans"),

]