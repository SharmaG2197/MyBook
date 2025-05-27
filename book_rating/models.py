from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator

class BookRating(models.Model):
  id = models.AutoField(primary_key=True)
  user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  book = models.ForeignKey('books.Book', on_delete=models.CASCADE, related_name='ratings')
  rating = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
  comment = models.TextField(blank=True, null=True)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  class Meta:
    unique_together = ('user', 'book')  # Each user can rate a book only once
    ordering = ['-created_at']

  def __str__(self):
    return f"{self.user.email} rated {self.book.id} - {self.rating} stars"

# C:\Users\v-deepak.sharma\Desktop\BOOK\venv\my_book\book_rating