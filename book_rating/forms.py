from django import forms
from .models import BookRating

class RatingForm(forms.ModelForm):
  class Meta:
    model = BookRating
    fields = ['rating', 'comment']
    widgets = { 'rating': forms.NumberInput(attrs={ 'min': 1, 'max': 5, 'class': 'form-control' }),
                'comment': forms.Textarea(attrs={ 'class': 'form-control', 'rows': 3, 'placeholder': 'Share your thoughts about this book...'})
              }

    def clean(self):
      cleaned_data = super().clean()
      rating = cleaned_data.get('rating')
      comment = cleaned_data.get('comment')

      if not rating or not comment:
        raise forms.ValidationError("Both rating and comment are required.")
