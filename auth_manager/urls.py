from rest_framework.authtoken.views import obtain_auth_token
from django.contrib import admin
from django.urls import path, include
from auth_manager.views import RegisterAPI, LogoutView

urlpatterns = [
    path('login', obtain_auth_token, name='login'),
    path('register', RegisterAPI.as_view(), name='register'),
    path(r'logout', LogoutView.as_view())
]