from django.shortcuts import render

def home(request):
    return render(request, 'news/new.html')  # Убедитесь, что шаблон существует!