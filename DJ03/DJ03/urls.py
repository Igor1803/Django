from django.contrib import admin
from django.urls import path, include
from news import views  # Импортируем views из приложения news

urlpatterns = [
    path('admin/', admin.site.urls),
    path('news/', include('news.urls')),  # Маршруты приложения news
    path('', views.home, name='home'),    # Корневой путь (главная страница)
]
