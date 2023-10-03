from django.urls import path
from . import views

urlpatterns = [
    path("home", views.home, name="home"),
    path("register_user/", views.register_user, name="register_user"),
    path("logout_user/", views.logout_user, name="logout_user"),
    path("products/", views.products, name="products"),
]

