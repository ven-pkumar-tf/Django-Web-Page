from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import SignUpForm
from .models import User, Event
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login
from home.backend import CustomBackend  # Import your custom backend
from django.contrib.auth.decorators import login_required

# Ensure this view exists
def profile(request):
    return render(request, 'home/profile.html')
def event_details(request):
    events = Event.objects.all()
    print("Number of Events:", events.count())  # Check if events are being fetched
    print("Events:", events)  # Check if events data is being fetched correctly
    if not events:
        print("No events found!")  # This will print if events are empty
    return render(request, 'home/home.html', {'events': events})

def home_page(request):
    return render(request, 'home/home.html')


# View for Login page
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        # Use CustomBackend for authentication
        backend = CustomBackend()
        user = backend.authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, 'You are now logged in.')
            return redirect('home')
        else:
            messages.error(request, 'Invalid credentials, please try again.')
    
    return render(request, 'home/login.html')


# View for Signup page
def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            # Save the user data into the database
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = make_password(form.cleaned_data['password'])
            user_role = form.cleaned_data['user_role']
            
            # Create and save the user
            user = User.objects.create(username=username, email=email, password=password, user_role=user_role)
            
            # Provide a success message and redirect to login page
            messages.success(request, 'Account created successfully! You can now log in.')
            return redirect('login')
    else:
        form = SignUpForm()

    return render(request, 'home/signup.html')
