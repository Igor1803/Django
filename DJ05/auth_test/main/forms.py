# from django.contrib.auth.forms import UserCreationForm
# from .models import User
#
# class CustomUserCreationForm(UserCreationForm):
#     class Meta(UserCreationForm.Meta):
#         model = User
#         # Поля, которые будут отображаться в форме регистрации.
#         # username — обязательно, email и phone_number добавлены.
#         fields = ('username', 'email', 'phone_number')

from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser  # Импорт изменен с User → CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser  # Указана новая модель
        fields = ('username', 'email', 'phone_number')  # Поля соответствуют заданию
