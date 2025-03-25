#home/urls.py
from django.urls import path
from . import views  # Ensure that views are imported correctly

urlpatterns = [
    path('', views.home_page, name='home'),  # Home page URL
    path('login/', views.login_view, name='login'),  # Login page URL
    path('signup/', views.signup_view, name='signup'),  # Signup page URL
    path('profile/', views.profile, name='profile'),
]
