from pyexpat.errors import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

# Create your views here.

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('404')
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'account/login.html')

def register(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if password1 != password2:
            messages.error(request, 'Passwords do not match')
        if User.objects.filter(username=email).exists():
            messages.error(request, 'Email already exists')
        user = User.objects.create_user(username=email, email=email, password=password1, first_name=full_name)
        user.save()
        messages.success(request, 'Registration successful')
        return redirect('login')
    return render(request, 'account/register.html')