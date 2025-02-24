from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import JsonResponse
from .models import Lesson, Quiz, Tag, Comment, Note, UserProfile, BookmarkedLesson
from .forms import LessonForm, CustomUserCreationForm, CustomLoginForm
import logging

logger = logging.getLogger(__name__)

# Utility Functions
def get_user_group(user):
    """Returns the first group name of the user."""
    return user.groups.values_list("name", flat=True).first()


# Public Views
def landing_view(request):
    user_group = get_user_group(request.user) if request.user.is_authenticated else None
    grammar_lessons = Lesson.objects.filter(tags__name="Grammar").select_related('created_by').order_by('-created_at')[:3]
    logger.debug(f"Retrieved {len(grammar_lessons)} grammar lessons")
    return render(request, 'landing.html', {'user_group': user_group, 'grammar_lessons': grammar_lessons})


def preview_lesson(request, lesson_id):
    lesson = get_object_or_404(Lesson, id=lesson_id)
    return render(request, 'preview_lesson.html', {'lesson': lesson})


def about_view(request):
    return render(request, "about.html")


def signup_view(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            avatar_choice = form.cleaned_data.get('avatar')
            if avatar_choice in dict(form.fields['avatar'].choices):
                UserProfile.objects.create(user=user, avatar=avatar_choice)
                logger.info(f"UserProfile created for {user.username} with avatar {avatar_choice}")
            login(request, user)
            return redirect('student_dashboard')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})


def login_view(request):
    form = CustomLoginForm(data=request.POST) if request.method == "POST" else CustomLoginForm()
    if request.method == 'POST' and form.is_valid():
        user = form.get_user()
        login(request, user)
        if user.groups.filter(name='Content Creators').exists():
            return redirect('creator_dashboard')  
        return redirect('student_dashboard')  
    return render(request, 'registration/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('landing')

# Group Check Functions
def is_content_creator(user):
    return user.groups.filter(name='Content Creators').exists()

def is_student(user):
    return user.groups.filter(name='Students').exists()

# Content Creator Views
@login_required
@user_passes_test(is_content_creator)
def creator_dashboard(request):
    return render(request, 'dashboard/creator_dashboard.html')

@login_required
@user_passes_test(is_content_creator)
def view_lessons_quizzes(request):
    sort_lessons = request.GET.get("sort_lessons", "-updated_at")
    lessons = Lesson.objects.filter(created_by=request.user).order_by(sort_lessons)
    sort_quizzes = request.GET.get("sort_quizzes", "-updated_at")
    quizzes = Quiz.objects.filter(created_by=request.user).order_by(sort_quizzes)
    return render(request, "contentCreator/view_lessons_quizzes.html", {"lessons": lessons, "quizzes": quizzes})

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




# Student Views
@login_required
@user_passes_test(is_student)
def student_dashboard(request):
    bookmarked_lessons = Lesson.objects.filter(bookmarked_by_users__user=request.user)

    return render(request, 'dashboard/student_dashboard.html', {
        'bookmarked_lessons': bookmarked_lessons
    })


@login_required
def lesson_search(request):
    query = request.GET.get("q", "")
    tag_filter = request.GET.getlist("tags")

    lessons = Lesson.objects.all()

    if query:
        lessons = lessons.filter(
            Q(title__icontains=query) | 
            Q(preview__icontains=query) | 
            Q(content__icontains=query)
        )

    if tag_filter:
        lessons = lessons.filter(tags__id__in=tag_filter).distinct()

    tags = Tag.objects.all()

    # ✅ Precompute bookmarked lessons for the current user
    bookmarked_lessons = set(BookmarkedLesson.objects.filter(user=request.user).values_list('lesson_id', flat=True))

    return render(request, "student/lesson_search.html", {
        "lessons": lessons,
        "tags": tags,
        "query": query,
        "selected_tags": tag_filter,
        "bookmarked_lessons": bookmarked_lessons  # ✅ Pass precomputed bookmarks
    })

@login_required
def lesson_view(request, lesson_id):
    lesson = get_object_or_404(Lesson, id=lesson_id)
    comments = Comment.objects.filter(lesson=lesson)
    notes = Note.objects.filter(lesson=lesson, user=request.user)

    # ✅ Ensure we check if the lesson is bookmarked by the user
    is_bookmarked = BookmarkedLesson.objects.filter(user=request.user, lesson=lesson).exists()

    return render(request, "student/lesson_view.html", {
        "lesson": lesson,
        "comments": comments,
        "notes": notes,
        "is_bookmarked": is_bookmarked,  # ✅ Pass the bookmark status to the template
    })

@login_required
def add_comment(request, lesson_id):
    if request.method == "POST":
        lesson = get_object_or_404(Lesson, id=lesson_id)
        comment_text = request.POST.get("text", "").strip()
        if comment_text:
            Comment.objects.create(lesson=lesson, user=request.user, text=comment_text)
    return redirect("lesson_view", lesson_id=lesson_id)

@login_required
def add_note(request, lesson_id):
    if request.method == "POST":
        lesson = get_object_or_404(Lesson, id=lesson_id)
        note_text = request.POST.get("text", "").strip()
        if note_text:
            Note.objects.create(lesson=lesson, user=request.user, text=note_text)
    return redirect("lesson_view", lesson_id=lesson_id)


@login_required
def toggle_bookmark(request, lesson_id):
    lesson = get_object_or_404(Lesson, id=lesson_id)
    
    # Check if the lesson is already bookmarked
    bookmark, created = BookmarkedLesson.objects.get_or_create(user=request.user, lesson=lesson)

    if not created:
        # If bookmark already exists, remove it (unbookmark)
        bookmark.delete()
        bookmarked = False
    else:
        bookmarked = True

    return JsonResponse({"bookmarked": bookmarked})