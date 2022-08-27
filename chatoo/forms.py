from django.db import models
from django.forms import fields
from django.contrib.auth.models import User
from django import forms
from .models import Chat, Pictures, Profile

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username', 'email', 'password',)
        
class PicturesForm(forms.ModelForm):
     class Meta():
         model = Pictures
         fields = ('photo',)

class ProfileForm(forms.ModelForm):
     class Meta():
         model = Profile
         fields = ('photo',)


class ChatForm(forms.ModelForm):
    body = forms.CharField(required=True, widget=forms.widgets.Textarea(
            attrs={
                "placeholder": "write something...",
                "class": "textarea is-success is-medium",
            }
        ),
        label="",)

    class Meta:
        model = Chat
        exclude = ("user", )