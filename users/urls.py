from django.urls import path
from .views import *

urlpatterns = [
    path('', UserList.as_view(), name='user_list'),
    path('<int:pk>/', UserDetail.as_view(), name='user_detail'),
]