from django.contrib import admin
from .models import BookRating

class BookRatingAdmin(admin.ModelAdmin):
  list_display = ('id', 'user', 'book', 'rating', 'comment')

admin.site.register(BookRating, BookRatingAdmin)


# C:\Users\v-deepak.sharma\Desktop\BOOK\venv\my_book\book_rating\admin.py
