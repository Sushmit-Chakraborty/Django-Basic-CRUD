from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['postTitle','postContent']
        
        widgets = {
            'postContent': forms.Textarea(attrs={'rows': 4, 'cols': 40}),
        }
        labels = {
            'postTitle': 'Title',
            'postContent': 'Content',
        }