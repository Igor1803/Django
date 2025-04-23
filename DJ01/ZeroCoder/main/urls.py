from django.urls import path
from . import views  # Импорт views один раз

urlpatterns = [
    path('', views.index),    # Главная страница
    path('new/', views.new),   # Страница /new/
    path('data/', views.data),
    path('test/', views.test)
]