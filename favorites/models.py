from django.db import models
from django.conf import settings
from books.models import Book  # adjust import if needed

class Favorite(models.Model):
  user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  book = models.ForeignKey(Book, on_delete=models.CASCADE)
  created_at = models.DateTimeField(auto_now_add=True)

  class Meta:
    unique_together = ('user', 'book')  # prevent duplicate favorites

  def __str__(self):
    return f"{self.user.email} ❤️ {self.book.id}"
