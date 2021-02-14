from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from loginapp.models import UserProfile

class SignupForm(UserCreationForm):
    email = forms.EmailField(label="Email Address", required=True)
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class ProfileChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password')

class ProfilepicForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['profile_pic',]
