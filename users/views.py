from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.urls import reverse_lazy
from .forms import UserRegister
# from django.contrib.auth.views import PasswordChangeView, PasswordResetView, PasswordResetDoneView,PasswordResetConfirmView
from .forms import ChangePassword
# Create your views here.

class UserRegisterView(generic.CreateView):

	form_class = UserRegister
	template_name = 'registration/register.html'
	success_url = reverse_lazy('login')