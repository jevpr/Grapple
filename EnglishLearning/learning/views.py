from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import Group
from .models import Lesson, Quiz, Question, Option, UserProgress, UserProfile
from .forms import LessonForm, CustomUserCreationForm, CustomLoginForm


#Landing page
def landing_view(request):
    return render(request, 'landing.html')


#About page
def about_view(request):
    return render(request, "about.html")

#Signup page
def signup_view(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()

            avatar_choice = form.cleaned_data.get('avatar')

            valid_avatars = [choice[0] for choice in form.fields['avatar'].choices]
            if avatar_choice in valid_avatars:
                UserProfile.objects.create(user=user, avatar=avatar_choice)  # Create profile
                print(f"Debug: UserProfile created for {user.username} with avatar {avatar_choice}")
            else:
                print(f"ERROR: Invalid avatar choice recieved: {avatar_choice}")   

            login(request, user)
            
            return redirect('student_dashboard')  # Redirect to student dashboard by default
    else:
        form = CustomUserCreationForm()

    return render(request, 'registration/signup.html', {'form': form})


#Login page with redirection based on role
def login_view(request):
    form = CustomLoginForm(data=request.POST) if request.method == "POST" else CustomLoginForm()

    if request.method == 'POST' and form.is_valid():
        user = form.get_user()
        login(request, user)

        if user.groups.filter(name='Content Creators').exists():
            return redirect('creator_dashboard')  
        elif user.groups.filter(name='Students').exists():
            return redirect('student_dashboard')  
        else:
            return redirect('landing')

    return render(request, 'registration/login.html', {'form': form})
#Need to create an option for when the user doesn't exist in the database.


#Logout view
def logout_view(request):
    logout(request)
    return redirect('landing')


#Group check functions
def is_content_creator(user):
    return user.groups.filter(name='Content Creators').exists()

def is_student(user):
    return user.groups.filter(name='Students').exists()


#Dashboards
@login_required
@user_passes_test(is_content_creator)
def creator_dashboard(request):
    return render(request, 'dashboard/creator_dashboard.html')

@login_required
@user_passes_test(is_student)
def student_dashboard(request):
    return render(request, 'dashboard/student_dashboard.html')




