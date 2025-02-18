from django import forms
from .models import Lesson, Tag
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django_ckeditor_5.widgets import CKEditor5Widget

#Creating a new user
class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={
            'placeholder': 'Username',
            'class': 'form-control'
            })
    )
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
            'placeholder': 'Email',
            'class': 'form-control'
            })
    )
    password1 = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Enter Password',
            'class': 'form-control'
            })
    )
    password2 = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Confirm Password',
            'class': 'form-control'
            })
    )
    avatar = forms.ChoiceField(
        choices=[
            ('avatar1.png', 'Avatar 1'),
            ('avatar2.png', 'Avatar 2'),
            ('avatar3.png', 'Avatar 3'), 
            ('avatar4.png', 'Avatar 4'),
            ('avatar5.png', 'Avatar 5'),
        ],
        widget=forms.RadioSelect
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'avatar']


#Signing in a user
class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={
            'placeholder': 'Username',
            'class': 'form-control'
        })
    )
    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Enter Password',
            'class': 'form-control'
        })
    )

#Creating a lesson
class LessonForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True
    )

    content = forms.CharField(
        widget=CKEditor5Widget(config_name="default"),  # ✅ Apply CKEditor
        required=True
    )

    class Meta:
        model = Lesson
        fields = ["title", "tags", "content"]
        widgets = {
            "title": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Lesson Title",  # ✅ Already has a placeholder
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # ✅ Remove labels by setting them to empty strings
        self.fields["title"].label = ""
        self.fields["content"].label = ""