from django import forms
from .models import *
class NewTopicForm(forms.ModelForm):
    message=forms.CharField(widget=forms.Textarea(attrs={'rows':5,'placeholder':'What is your mind?'}),max_length=4000,help_text='max length is 4000 character')
    class Meta:
        model=Topic
        fields=['subject','message']

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields=['message',]
