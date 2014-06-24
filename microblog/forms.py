from django import forms
from models import Post

class PostForm(forms.ModelForm):
    
    class Meta:
        model = Post
        # Controls which fields should be filled in on our 'create' page.
        # Fields not included here should have a default value 
        # or should be dealt with in the model's save function.
        fields = ('title', 'content', 'published', 'author')
