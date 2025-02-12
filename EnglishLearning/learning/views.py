from django.shortcuts import render, redirect, get_object_or_404
from .models import Lesson, Quiz, Question, Option, UserProgress
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required, user_passes_test
from .forms import LessonForm, CustomUserCreationForm


def landing_view(request):
    return render(request, 'landing.html')

def home(request):
    return render(request, "base.html")

def about_view(request):
    return render(request, "about.html")


from .models import UserProfile

def signup_view(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()

            avatar_choice = form.cleaned_data.get('avatar')
            print(f"Avatar choice: {avatar_choice}")

            valid_avatars = [choice[0] for choice in form.fields['avatar'].choices]
            if avatar_choice in valid_avatars:
                UserProfile.objects.create(user=user, avatar=avatar_choice)  # Create profile
                print(f"Debug: UserProfile created for {user.username} with avatar {avatar_choice}")
            else:
                print(f"ERROR: Invalid avatar choice recieved: {avatar_choice}")   

            login(request, user)
            return redirect('home')
    else:
        form = CustomUserCreationForm()

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




