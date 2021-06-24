from django.shortcuts import render
from .models import Book
from django.utils import timezone
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    return render(request, "books/home.html")

def book_info(request):
    books = Book.objects.filter(created_at__lte=timezone.now()).order_by('created_at')
    return render(request, 'books/login.html', {'books': books})

@login_required()
def book_list(request):
    book_display = 



def all_links(request):
    return render(request, 'books/base.html')