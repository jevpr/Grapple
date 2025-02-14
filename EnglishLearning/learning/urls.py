from django.urls import path, include
from . import views
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('', views.landing_view, name='landing'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('about/', views.about_view, name='about'),

    #Content creator dashboard and actions
    path("ckeditor5/", include('django_ckeditor_5.urls')),
    path('dashboard/creator/', views.creator_dashboard, name='creator_dashboard'),
    path('dashboard/creator/view/', views.view_lessons_quizzes, name='view_lessons_quizzes'),
    path('dashboard/creator/lesson/create/', views.create_lesson, name='create_lesson'),
    path('dashboard/creator/quiz/create/', views.create_quiz, name='create_quiz'),

    #Student dashboard and actions
    path('dashboard/student/', views.student_dashboard, name='student_dashboard'),
]

