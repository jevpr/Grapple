from django.urls import path
from . import views
from .views import quiz_detail


urlpatterns = [
    path('', views.dashboard_view, name='dashboard'),
    path('create-lesson/', views.create_lesson, name='create_lesson'),
    path('lesson/<int:lesson_id>/', views.lesson_detail, name='lesson_detail'),
    path('quiz/<int:quiz_id>/', quiz_detail, name='quiz_detail'),

]

