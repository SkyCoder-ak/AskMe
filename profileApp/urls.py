from django.urls import path
from . import views

urlpatterns = [
    path('dashboard', views.profileView),
    path('edit-profile', views.editProfileView),
    path('followers', views.followersView),
    path('followings', views.followingsView),
    path('user-questions', views.userQueView),
    path('user-answers', views.userAnsView),
]