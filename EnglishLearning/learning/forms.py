from django import forms
from .models import Lesson, Quiz

class LessonForm(forms.ModelForm):
    quizzes = forms.ModelChoiceField(
        queryset=Quiz.objects.all(),
        required=False,
        empty_label='--Select a quiz to insert--'
    )

    class Meta: 
        model = Lesson
        fields= ['title', 'content']

