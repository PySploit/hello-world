from django import forms
from ckeditor.fields import RichTextField
from .models import Category, Post

class PostStoryForm(forms.ModelForm):

	class Meta:

		model = Post
		fields = ('author', 'category', 'title', 'title_tag', 'header_image', 
			'image_source', 'body')

		widgets = {

			'author':forms.Select(attrs={'class':'form-control', 'placeholder':'username', 'value':'', 'id':'myauthor'}),
			'title':forms.TextInput(attrs={'class':'form-control'}),
			'title_tag':forms.TextInput(attrs={'class':'form-control'}),
			'category':forms.TextInput(attrs={'class':'form-control'}),
			'image_source':forms.TextInput(attrs={'class':'form-control', 'placeholder':'If not personal image, enter url or site downloaded from'}),
			'body':forms.Textarea(attrs={'class':'form-control'}),
			# 'date_created':forms.DateTimeField(attrs={'class':'form-control'}),
			# 'date_updated':forms.DateTimeField(attrs={'class':'form-control'}),

		}

class EditStoryForm(forms.ModelForm):

	class Meta:

		model = Post
		fields = ('category', 'title', 'title_tag', 'header_image', 'image_source',
			'body')

		widgets = {
		
			'title':forms.TextInput(attrs={'class':'form-control'}),
			'title_tag':forms.TextInput(attrs={'class':'form-control'}),
			'category':forms.TextInput(attrs={'class':'form-control'}),
			'body':forms.Textarea(attrs={'class':'form-control'}),
			# 'date_created':forms.DateTimeField(attrs={'class':'form-control'}),
			# 'date_updated':forms.DateTimeField(attrs={'class':'form-control'}),

		}