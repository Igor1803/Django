from django.urls import path
from . import views

urlpatterns = [
   path('', views.home, name='news_home'),
   # path('', views.index, name='index'),
]
