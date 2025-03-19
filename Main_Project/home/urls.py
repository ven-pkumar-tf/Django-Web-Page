from django.urls import path
from . import views  # Make sure to import views

urlpatterns = [
    path('', views.home_page, name='home'),  # Home page
    path('signup/', views.signup_view, name='signup'),  # Signup page
    path('login/', views.login_view, name='login'),  # Login page
]
