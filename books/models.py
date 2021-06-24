from django.db.models.fields import NullBooleanField
from django_freeshelf.settings import TEMPLATES
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

class User(AbstractUser):
    def __repr__(self):
        return f"<User username={self.username}>"

    def __str__(self):
        return self.username

class Book(models.Model):
    title = models.CharField(max_length=100, help_text='Book Title')
    author = models.CharField(max_length=100, help_text='Book Author')
    description = models.TextField()
    book_link = models.CharField(max_length= 100, help_text='Book Link')
    created_at = models.DateTimeField( auto_now=False, auto_now_add=True, verbose_name = "Created on")
    image = models.URLField(null=True, blank=True)

    def __str__(self):
        return "%s (%s)" % (self.Book.title, self.image)