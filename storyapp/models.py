from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from datetime import datetime, date
# Create your models here.


class Category(models.Model):

	name = models.CharField(max_length=255)

	def __str__(self):
		return self.name

	# def get_absolute_url(self):

	# 	return reverse('blog')


class Post(models.Model):
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	title = models.CharField(max_length=255)
	title_tag = models.CharField(max_length=255)
	header_image = models.ImageField(upload_to='header_image/')
	image_source = models.CharField(max_length=255)
	category = models.CharField(max_length=255)
	body = RichTextField()
	publish_date = models.DateTimeField(auto_now_add=True)
	updated_on = models.DateTimeField(auto_now=True)

	def __str__(self):

		return self.title + " | " + self.author.last_name + " " + self.author.first_name


	def get_absolute_url(self):

		return reverse('story-detail', args=[self.id,])