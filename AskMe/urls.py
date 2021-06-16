"""AskMe URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from os import name
import homeApp
from django.contrib import admin
from django.urls import path,include
from homeApp import views as homeviews
from signupApp import views as signupviews
from loginApp import views as loginviews
from AboutUs import views as aboutviews
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homeviews.homeView, name='home'),
    path('home/', include('homeApp.urls')),
    path('peoples/', homeviews.peoplesView),
    path('signup/', signupviews.signupView),
    path('login/', loginviews.loginView),
    path('about-us/', aboutviews.AboutView, name='aboutpage'),
    path('profile/', include('profileApp.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
