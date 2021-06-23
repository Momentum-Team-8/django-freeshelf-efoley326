import os
from django.conf import settings

file_ = open(os.path.join(settings.BASE_DIR, 'filename'))

from django.shortcuts import render
from .models import Book
from django.utils import timezone

# Create your views here.


def book_info(request):
    book = Book.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
    return render(request, 'books/book_list.html', {'book': book})
