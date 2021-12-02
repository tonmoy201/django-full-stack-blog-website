from django import forms
from django.db.models import fields
from django.forms import models 
from app_blog.models import Blog,Comment,Like

class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields=('comment',)