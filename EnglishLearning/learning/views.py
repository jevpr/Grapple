from django.shortcuts import render, redirect, get_object_or_404
from django.utils.html import strip_tags
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import Group
from django.core.paginator import Paginator
from .models import Lesson, Quiz, Tag, Question, Option, UserProgress, UserProfile
from .forms import LessonForm, CustomUserCreationForm, CustomLoginForm


#one problem with the code is that when I'm logged in as a content creator, if i do end up on the landing page
#it has login in the nav bar, but shows the landing page html

#Landing page
def landing_view(request):
    user_group = None  # Default value for non-logged-in users

    if request.user.is_authenticated:
        if request.user.groups.filter(name="Content Creators").exists():
            user_group = "Content Creators"
        elif request.user.groups.filter(name="Students").exists():
            user_group = "Students"
    
    # Fetch the latest lessons for specific tags
    grammar_tag = Tag.objects.filter(name="Grammar").first()
    grammar_lessons = []
    
    if grammar_tag:
        lessons = Lesson.objects.filter(tags=grammar_tag).order_by('-created_at')[:3]  # Get 3 most recent lessons
        for lesson in lessons:
            preview = strip_tags(lesson.content)[:100] + "..." if lesson.content else "No content available."
            grammar_lessons.append({"lesson": lesson, "preview": preview})

    return render(request, 'landing.html', {
        'user_group': user_group,
        'grammar_lessons': grammar_lessons
    })




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


#Content Creator permissions
@login_required
@user_passes_test(is_content_creator)
def creator_dashboard(request):
    return render(request, 'dashboard/creator_dashboard.html')

@login_required
@user_passes_test(is_content_creator)
def view_lessons_quizzes(request):
    return render(request, 'contentCreator/view_lessons_quizzes.html')

@login_required
@user_passes_test(is_content_creator)
def create_lesson(request):
    return render(request, 'contentCreator/create_lesson.html')

@login_required
@user_passes_test(is_content_creator)
def create_quiz(request):
    return render(request, 'contentCreator/create_quiz.html')


#Lessons and quizzes, view lists
def view_lessons_quizzes(request):
    sort_lessons = request.GET.get("sort_lessons", "-updated_at")
    lessons = Lesson.objects.filter(created_by=request.user).order_by(sort_lessons)

    sort_quizzes = request.GET.get("sort_quizzes", "-updated_at")
    quizzes = Quiz.objects.filter(created_by=request.user).order_by(sort_quizzes)

    paginator_lessons = Paginator(lessons, 10)
    page_number_lessons = request.GET.get('page_lessons')
    lessons_page = paginator_lessons.get_page(page_number_lessons)

    paginator_quizzes = Paginator(quizzes, 10)
    page_number_quizzes = request.GET.get('page_quizzes')
    quizzes_page = paginator_quizzes.get_page(page_number_quizzes)

    return render(
        request,
        "contentCreator/view_lessons_quizzes.html",
        {
            "lessons": lessons_page,
            "quizzes": quizzes_page,
        },
    )



def view_lesson(request, lesson_id):
    lesson = get_object_or_404(Lesson, id=lesson_id)
    return render(request, 'contentCreator/view_lesson.html', {'lesson': lesson})


def edit_lesson(request, lesson_id):
    lesson = get_object_or_404(Lesson, id=lesson_id)

    if request.method == "POST":
        form = LessonForm(request.POST, instance=lesson)
        if form.is_valid():
            form.save()
            return redirect('view_lessons_quizzes')
    else:
        form = LessonForm(instance=lesson)

    return render(request, 'contentCreator/create_lesson.html', {'form': form, 'lesson': lesson})


def delete_lesson(request, lesson_id):
    lesson = get_object_or_404(Lesson, id=lesson_id)

    if request.method == "POST":
        lesson.delete()
        messages.success(request, f"Lesson '{lesson.title}' deleted successfully.")
        return redirect('view_lessons_quizzes')
    
    return redirect('view_lessons_quizzes')

#Student permissions
@login_required
@user_passes_test(is_student)
def student_dashboard(request):
    return render(request, 'dashboard/student_dashboard.html')




#Creating a lesson
@login_required
@user_passes_test(is_content_creator)
def create_lesson(request):
    if request.method == "POST":
        form = LessonForm(request.POST)
        if form.is_valid():
            lesson = form.save(commit=False)
            lesson.created_by = request.user
            lesson.save()
            return redirect('view_lessons_quizzes')
    else:
        form = LessonForm()

    return render(request, 'contentCreator/create_lesson.html', {'form': form})




