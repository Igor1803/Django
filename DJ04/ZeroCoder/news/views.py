from django.shortcuts import render
from .models import News_post
from .forms import New_postForm

def home(request):
    news = News_post.objects.all()
    return render(request, 'news/news.html', {'news': news})

def create_news(request):
	return render(request, 'news/add_new_post.html', {'form': form})
