from .models import User, Comment
from django.forms import ModelForm, TextInput
from django import forms
from .models import CRUD



class CRUDCreate(forms.ModelForm):
    class Meta:
        model = CRUD
        fields = '__all__'


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ["username", "email", "password"]
        widgets = {
            "username": TextInput(attrs={
                'class': 'form__input',
                'placeholder': 'Username'
            }),
            "email": TextInput(attrs={
                'class': 'form__input',
                'placeholder': 'Email'
            }),
            "password": TextInput(attrs={
                'class': 'form__input',
                'placeholder': 'Пароль'
            }),
        }


class UserComment(ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'
        #fields = ["comment", "email"]
        widgets = {
            "comment": TextInput(attrs={
                'class': 'form-otzyv',
                'placeholder': 'Напишите что думаете о нашем магазине'
            }),
            "email": TextInput(attrs={
                'class': 'form-otzyv',
                'placeholder': 'Email'
            }),
        }
