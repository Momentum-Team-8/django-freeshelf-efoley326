from django.contrib import admin
from .models import User, book_info

# Register your models here.
admin.site.register(User)
admin.site.register(book_info)