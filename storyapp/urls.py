from django.urls import path
from .views import HomeView, StoryView, StoryDetailView, CategoryView, CreateStory, DeleteStory, UpdateStory
urlpatterns = [

	path('', HomeView.as_view(), name='home'),
	path('stories/', StoryView.as_view(), name='stories'),
	path('category/<str:cats>', CategoryView, name="category"),
	path('story/<int:pk>', StoryDetailView.as_view(), name='story-detail'),
	path('creating-story/', CreateStory.as_view(), name='create-story'),
	path('Delete/story/<int:pk>', DeleteStory.as_view(), name='delete-story'),
	path('Editing/story/<int:pk>/', UpdateStory.as_view(), name='edit-story'),
]


