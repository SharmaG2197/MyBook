from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
  list_display = ('id', 'title', 'user', 'author', 'condition', 'total_price', 'discount_price')

admin.site.register(Book, BookAdmin)
