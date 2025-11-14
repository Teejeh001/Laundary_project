from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def login (request):
    return render(request, 'login.html')

def signup (request):
    return render(request, 'signup.html')

def dashboard (request):
    return render(request, 'dashboard.html')

def landing (request):
    return render(request, 'landing.html')

def service (request):
    return render(request, 'service.html')

def pricing (request):
    return render(request, 'pricing.html')

def logout (request):
    return render(request, 'logout.html')

def booking (request):
    return render(request, 'booking.html')


def contact (request):
    return render(request, 'contact.html')