from django.urls import path, include
from .views import *
from . import views
from rest_framework_simplejwt.views import (TokenObtainPairView,TokenRefreshView,TokenVerifyView,)

urlpatterns = [ 
    # path('api/token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    # path('api/token/verify', TokenVerifyView.as_view(), name='token_verify'),
    path('auth/register', views.AdminRegisterationAPIView.as_view()),
    path('admin/login', views.LoginAPIView.as_view()),
    path('user/create-role', views.RoleCreateAPIView.as_view()),
    path('admin/create-module', views.CreateModuleAPIView.as_view()),
    path('admin/create-module-permission', views.CreateModulePermissionAPIView.as_view()),
    path('admin/module-permissions', views.CreateModulePermissionListAPIView.as_view()),
    path('admin/create-user-profile', views.CreateUserProfileAPIView.as_view()),
    path('admin/user-profile-lists', views.UserProfileListAPIView.as_view()),


]
