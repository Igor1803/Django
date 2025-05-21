
from django.contrib import admin
from django.urls import path
from bot.views import register_user, get_user_info
from django.http import HttpResponse

def home(request):
    return HttpResponse("Добро пожаловать в Django + Telegram Bot API!")
    
urlpatterns = [
    path('', home),  # Добавьте эту строку
    path('admin/', admin.site.urls),
    path('api/register/', register_user),
    path('api/user/<int:user_id>/', get_user_info),
]




