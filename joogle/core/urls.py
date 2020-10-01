from django.contrib import admin
from django.urls import path, include
from knox import views as knox_views
from core.views import RegisterAPI, LoginAPI, MobileUserRegisterAPI, MobileUserLoginAPI

urlpatterns = [
    path('auth', include('knox.urls')),
    path('adminuser/auth/register', RegisterAPI.as_view()),
    path('adminuser/auth/login', LoginAPI.as_view(), name='customized_login'),

    path('mobileuser/auth/register', MobileUserRegisterAPI.as_view()),
    path('mobileuser/auth/login', MobileUserLoginAPI.as_view(), name='customized_mobile_user_login'),

    
    path('auth/logout', knox_views.LogoutView.as_view(), name='knox_logout'),
    path('auth/logoutall', knox_views.LogoutAllView.as_view(), name='knox_logoutall'),
]
