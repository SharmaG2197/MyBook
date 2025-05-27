from django.contrib import admin
from django.utils.html import format_html
from .models import Favorite

class FavoriteAdmin(admin.ModelAdmin):
  list_display = ('user', 'book_title_link')

  def book_title_link(self, obj):
    return format_html('<a href="/admin/books/book/{}/change/">{}</a>', obj.book.id, obj.book.title)
  book_title_link.short_description = 'Book'

admin.site.register(Favorite, FavoriteAdmin)
