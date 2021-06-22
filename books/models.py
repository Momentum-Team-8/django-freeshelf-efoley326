from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

class User(AbstractUser):
    def __repr__(self):
        return f"<User username={self.username}>"

    def __str__(self):
        return self.username




class book_info(models.Model):
    title = models.CharField(max_length=100, help_text='Book Title')
    author = models.CharField(max_length=100, help_text='Book Author')
    description = models.CharField(max_length=1000, help_text='Book Description')
    book_link = models.CharField(max_length= 100, help_text='Book Link')
    created_at = models.DateTimeField(max_length=20, help_text='book added at:')