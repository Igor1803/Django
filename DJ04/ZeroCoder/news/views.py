# from django.shortcuts import render, redirect
# from .models import News_post
# from .forms import New_postForm
#
# def home(request):
#     news = News_post.objects.all()
#     return render(request, 'news/news.html', {'news': news})
#
# def create_news(request):
#
# 	# if request.method == 'POST':
# 	# 	form = New_postForm(request.POST) # Сюда сохранится информация от пользователя.
# 	# 	if form.is_valid():
# 	# 		form.save()
# 	# 		return redirect('news_home')
# 	# 	else:
# 	# 		error = "Данные были заполнены некорректно"
# 	form = News_postForm()
# 	return render(request, 'news/add_new_post.html', {'form': form})#, 'error': error})

from django.shortcuts import render, redirect
from .models import News_post
from .forms import News_postForm  # Исправлено имя импорта


def home(request):
    news = News_post.objects.all()
    return render(request, 'news/news.html', {'news': news})


def create_news(request):
    if request.method == 'POST':
        form = News_postForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('news_home')
        else:
            error = "Данные были заполнены некорректно"
            return render(request, 'news/add_new_post.html', {'form': form, 'error': error})

    form = News_postForm()
    return render(request, 'news/add_new_post.html', {'form': form})