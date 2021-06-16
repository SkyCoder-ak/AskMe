from django.urls import path
from . import views

urlpatterns = [
    path('dashboard', views.profileView),
    path('edit-profile', views.editProfileView),
    path('followers/<int:f_id>', views.ProfileFollowView, name='follow_to'),
    path('followers', views.followersView, name='followers_main'),
    path('followings/<int:f_ing_id>', views.ProfileFollowingsView, name='follow_by'),
    path('followings', views.followingsView, name='followings_main'),
    path('user-questions', views.userQueView),
    path('user-answers', views.userAnsView),
    path('logout', views.logoutView),

]