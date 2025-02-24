from django.urls import path, include
from . import views
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('', views.landing_view, name='landing'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('about/', views.about_view, name='about'),
    path('preview_lesson/<int:lesson_id>/', views.preview_lesson, name='preview_lesson'),


    #Content creator dashboard and actions
    path("ckeditor5/", include('django_ckeditor_5.urls')),
    path('dashboard/creator/', views.creator_dashboard, name='creator_dashboard'),
    path('dashboard/creator/view/', views.view_lessons_quizzes, name='view_lessons_quizzes'),
    path('dashboard/creator/lesson/create/', views.create_lesson, name='create_lesson'),
    path('dashboard/creator/lesson/<int:lesson_id>/', views.view_lesson, name='view_lesson'),
    path('dashboard/creator/lesson/edit/<int:lesson_id>/', views.edit_lesson, name='edit_lesson'),
    path('dashboard/creator/lesson/delete/<int:lesson_id>/', views.delete_lesson, name='delete_lesson'),

    #Student dashboard and actions
    path('dashboard/student/', views.student_dashboard, name='student_dashboard'),
    path("lesson_search/", views.lesson_search, name="lesson_search"),
    path("lesson/<int:lesson_id>/", views.lesson_view, name="lesson_view"),
    path("lesson/<int:lesson_id>/comment/", views.add_comment, name="add_comment"),
    path("lesson/<int:lesson_id>/note/", views.add_note, name="add_note"),
]