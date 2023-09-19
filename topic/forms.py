from django import forms
from .models import Comment, Topic

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']


class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic  # Specify the model associated with this form
        fields = ['title', 'description']  # Define the fields you want in the form
