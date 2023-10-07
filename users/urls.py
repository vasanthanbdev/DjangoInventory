from django.urls import path, include
from .views import *

urlpatterns = [
    path("register_user/", register_user, name="register_user"),
    path("login_user/", login_user, name="login_user"),
    path("logout_user/", logout_user, name="logout_user"),
]

# app_name = 'users'

# urlpatterns = [
#     path('users/', include((urlpatterns, app_name), namespace=app_name))
# ]