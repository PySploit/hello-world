from django.shortcuts import render
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView
from .models import Category, Post
from django.urls import reverse_lazy
# Create your views here.

class HomeView(ListView):

	model = Post
	template_name = 'storyapp/index.html'

class StoryView(ListView):

	model = Post
	template_name = 'storyapp/stories.html'

	def get_context_data(self, *args, **kwargs):
		cat_menu = Category.objects.all()

		context = super(StoryView, self).get_context_data(*args, **kwargs)
		context['cat_menu'] = cat_menu
		return context

def CategoryView(request, cats):

	category_post = Post.objects.filter(category=cats.replace('-', ' '))

	return render(request, 'storyapp/categories.html', {'cats':cats.title().replace('-', ' '), 'category_post':category_post})

class StoryDetailView(DetailView):

	model = Post
	template_name = 'storyapp/story_detail.html'

class CreateStory(CreateView):

	model = Post
	template_name = 'storyapp/create_story.html'
	fields = '__all__'

class UpdateStory(UpdateView):

	model = Post
	template_name = 'storyapp/edit_story.html'
	fields = ['category', 'title', 'title_tag', 'header_image', 'image_source', 'body']

class DeleteStory(DeleteView):

	model = Post
	template_name = 'storyapp/delete_story.html'
	success_url = reverse_lazy('stories')