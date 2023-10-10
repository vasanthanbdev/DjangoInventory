from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import *

urlpatterns = [
    path('register_user/', RegisterUserView.as_view(), name='register_user'),
    path('login_user/', LoginView.as_view(template_name='login_user.html'), name='login_user'),
    path('logout_user/', LogoutView.as_view(template_name='logout_user.html'), name='logout_user'),
]