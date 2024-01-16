from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django import forms

from users.models import User

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': "form-control form-control-lg", 'placeholder': "Введите имя"
    }))

    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': "form-control form-control-lg" , 'placeholder': "Введите пароль"
    }))

    class Meta:
        model = User
        fields = ['username','password']

class UserRegistrationForm(UserCreationForm):

    email = forms.CharField(widget=forms.EmailInput(attrs={
        'class': "form-control form-control-lg", 'placeholder': "Введите эл. почту"
    }))
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': "form-control form-control-lg", 'placeholder': "Введите имя"
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': "form-control form-control-lg", 'placeholder': "Введите пароль"
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': "form-control form-control-lg", 'placeholder': "Введите пароль"
    }))

    class Meta:
        model = User
        fields = ['email','username','password1', 'password2']

class UserProfileForm(UserChangeForm):
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'class': "form-control form-control-lg", 'readonly': True
    }))
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': "form-control form-control-lg", 'readonly': True
    }))
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': "form-control form-control-lg"
    }))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': "form-control form-control-lg"
    }))
    image = forms.ImageField(widget=forms.FileInput(attrs={
        'class': "custom-file-input"
    }), required= False)



    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'image']