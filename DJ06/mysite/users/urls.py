from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_info, name='user_info'),
]
