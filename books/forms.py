from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'description', 'condition', 'total_price', 'discount_price', 'image']
        widgets = {
          'title': forms.TextInput(attrs={ 'class': 'form-control', 'placeholder': 'Enter book title' }),

          'author': forms.TextInput(attrs={ 'class': 'form-control', 'placeholder': 'Enter author name' }),

          'description': forms.Textarea(attrs={ 'class': 'form-control', 'placeholder': 'Enter book description', 'rows': 3 }),

          'condition': forms.Select(attrs={ 'class': 'form-select' }),

          'total_price': forms.NumberInput(attrs={ 'class': 'form-control', 'placeholder': 'Enter total price' }),

          'discount_price': forms.NumberInput(attrs={ 'class': 'form-control', 'placeholder': 'Enter discount price (if any)' }),

          'image': forms.FileInput(attrs={ 'class': 'form-control' }),
        }
