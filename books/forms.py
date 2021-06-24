from django.forms import ModelForm
from django.forms import forms
from .models import Book
from django.forms import User

class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = [
            'title', 
            'author',
            'book_link',
            'description',
            'created_at',
            'image',
            ]

    class UserCreationForm(forms.ModelForm):
        password1 = forms.CharField(label=_("Password"),
        widget=forms.PasswordInput)
        password2 = forms.CharField(label=_("Password confirmation"),
        widget=forms.PasswordInput,
        help_text=_("Enter the same password as above, for verification."))
        class Meta:
            model = User
            fields = ("username",)