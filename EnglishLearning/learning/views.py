from django.shortcuts import render, redirect, get_object_or_404
from .models import Lesson, Quiz, Question, Option, UserProgress
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required, user_passes_test
from .forms import LessonForm


def landing_view(request):
    return render(request, 'landing.html')

def home(request):
    return render(request, "base.html")

def about_view(request):
    return render(request, "about.html")


def signup_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Redirect after successful signup
    else:
        form = UserCreationForm()  # ✅ Initialize the form correctly

    return render(request, 'registration/signup.html', {'form': form})


def dashboard_view(request):
    return render(request, 'dashboard.html')

def login_view(request):
    form = AuthenticationForm(data=request.POST) if request.method == "POST" else AuthenticationForm()

    if request.method == 'POST' and form.is_valid():
        user = form.get_user()
        login(request, user)
        return redirect('home')
    
    return render(request, 'registration/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')



def is_content_creator(user):
    return user.groups.filter(name='Content Creators').exists()

@user_passes_test(is_content_creator)
def create_lesson(request):
    if request.method == "POST":
        form = LessonForm(request.POST)
        if form.is_valid():
            lesson = form.save(commit=False)
            quiz = form.cleaned_data.get('quizzes')
            if quiz:
                lesson.content += f"\n\n{{quiz_{quiz.id}}}"
            lesson.save()
            return redirect('lesson_detail', lesson_id=lesson.id)
    else:
        form = LessonForm()

    return render(request, 'learning/create_lesson.html', {'form': form})

def lesson_detail(request, lesson_id):
    lesson = get_object_or_404(Lesson, id=lesson_id)
    return render(request, 'learning/lesson_detail.html', {'lesson': lesson})

def quiz_detail(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)
    return render(request, 'learning/quiz_detail.html', {'quiz': quiz})




