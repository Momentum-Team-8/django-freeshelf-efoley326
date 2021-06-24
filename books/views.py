from django.shortcuts import render, redirect
from .models import Book
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def home(request):
    return render(request, "books/home.html")

def login_button(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
    return render(request, "books/home.html")

def register(request):
    if request.method == 'POST':
        f = UserCreationForm(request.POST)
        if f.is_valid():
            f.save()
            messages.success(request, 'Account created successfully')
            return redirect('register')

@login_required()
def book_info(request):
    books = Book.objects.filter(created_at__lte=timezone.now()).order_by('created_at')
    return render(request, 'books/home.html', {'books': books})

def library(request):
    return render(request, "books/home.html")

def all_links(request):
    return render(request, 'books/base.html')