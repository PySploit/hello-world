from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm

class UserRegister(UserCreationForm):

	email = forms.EmailField()
	first_name = forms.TextInput()
	last_name = forms.TextInput()

	class Meta:

		model = User
		fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

class ChangePassword(PasswordChangeForm):

	old_password = forms.PasswordInput()
	new_password1 =  forms.PasswordInput()
	new_password2 = forms.PasswordInput()

	class Meta:

		model = User
		fields = ['old_password', 'new_password1', 'new_password2']