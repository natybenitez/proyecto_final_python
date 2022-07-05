from django import forms
from posts.models import Blog_post

class Blog_post_form(forms.ModelForm):
    class Meta:
        model = Blog_post
        fields = '__all__'
