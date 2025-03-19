from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import ContactForm
from .models import EventDetails  # Assuming EventDetails model exists and contains event data
from django.contrib.auth.models import User


# Home Page View: Fetch events and render the home page
def home_page(request):
    events = EventDetails.objects.all()[:5]  # Fetch top 5 upcoming events
    return render(request, 'home/home.html', {'events': events})

# Contact View: Handle contact form submission
def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()  # Saves the form data in `contact_us_feedback` model
            return redirect('success')  # Redirect to a success page after form submission
    else:
        form = ContactForm()

    return render(request, 'home/contact_us.html', {'form': form})

# Login View: Handle user login
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        # Authenticate the user
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('profile')  # Redirect to the protected page (profile)
        else:
            messages.error(request, "Invalid username or password.")
            return redirect('login')  # Redirect back to login page
    else:
        return render(request, 'home/login.html')  # Render the login page if the request is GET

def signup_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        user_role = request.POST['user_role']  # Assuming user role is passed as well

        # Check if passwords match
        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return redirect('signup')

        # Create new user
        try:
            # Create and save user
            user = User(username=username, email=email, password=password, user_role=user_role)
            user.save()

            # Log the user in after successful signup
            return redirect('home')  # Redirect to the home page or any other page
        except Exception as e:
            messages.error(request, f"Error creating account: {e}")
            return redirect('signup')
    else:
        return render(request, 'home/signup.html')