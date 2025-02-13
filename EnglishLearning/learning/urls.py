from django.urls import path
from . import views
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('', views.landing_view, name='landing'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('about/', views.about_view, name='about'),
    path('dashboard/creator/', views.creator_dashboard, name='creator_dashboard'),
    path('dashboard/student/', views.student_dashboard, name='student_dashboard'),
]

