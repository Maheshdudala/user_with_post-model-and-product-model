from django.contrib.auth.models import User
from django import forms
class UserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','email','password','username']
from django import forms

from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)     