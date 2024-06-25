from django import forms
from .models import Profile
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

User = get_user_model()


class UserRegForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('email', 'username', 'first_name',
                  'last_name', 'password1', 'password2')


class UserLoginForm(AuthenticationForm):

    class Meta:
        model = get_user_model()
        fields = ('username', 'password')

    def __init__(self, request=None, *args, **kwargs):
        super().__init__(request, *args, **kwargs)
        self.fields['username'].label = 'Email | Username'
