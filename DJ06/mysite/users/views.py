from django.shortcuts import render
from .models import Profile

def user_info(request):
    users = Profile.objects.all()
    return render(request, 'users/user_info.html', {'users': users})
