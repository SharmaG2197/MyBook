from django.db import models
from django.conf import settings  # for referencing AUTH_USER_MODEL safely

CONDITION_CHOICES = (('new', 'New'), ('old', 'Old'))

class Book(models.Model):
  id = models.AutoField(primary_key=True)
  user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='books')
  title = models.CharField(max_length=255)
  description = models.TextField()
  author = models.CharField(max_length=255)
  total_price = models.DecimalField(max_digits=8, decimal_places=2)
  discount_price = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
  condition = models.CharField(max_length=20, choices=CONDITION_CHOICES, default='new')  # 👈 Add this line
  image = models.ImageField(upload_to='book_images/', blank=True, null=True)
  created_at = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.title
