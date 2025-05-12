from .models import New_post
from django.forms import ModelForm

class News_postForm(ModelForm):
	class Meta:
		model = New_post
		fields = ['title', 'short_description', 'text', 'pub_date']