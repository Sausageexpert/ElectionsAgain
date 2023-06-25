from django import forms
from .models import Questions

class QuestionForm(forms.Form):
    question = forms.CharField(max_length=500)
    answers = forms.CharField(max_length=500)