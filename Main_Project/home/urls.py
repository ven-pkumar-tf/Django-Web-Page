from django.urls import path
from .views import home_page

from django.shortcuts import render
from django.http import HttpResponse

urlpatterns = [
    path('', home_page, name='home'),
 
]



def home_page(request):
    if request.method == "POST":
        name = request.POST.get("name")
        contact_number = request.POST.get("contact_number")
        email = request.POST.get("email")
        message = request.POST.get("message")
        
        # Here you can save data to the database or send an email
        return HttpResponse("<h3>Thank you for contacting us!</h3>")

    return render(request, 'home/home.html')