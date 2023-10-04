from django.urls import path
from . import views

urlpatterns = [
    path("register_user/", views.register_user, name="register_user"),
    path("logout_user/", views.logout_user, name="logout_user"),
]