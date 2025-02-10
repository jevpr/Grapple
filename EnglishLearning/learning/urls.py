from django.urls import path
from . import views
from django.contrib.auth.views import LoginView
from .views import dashboard_view, quiz_detail

urlpatterns = [
    path('', dashboard_view, name='home'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'), 
]

