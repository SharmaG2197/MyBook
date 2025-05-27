from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from .models import Favorite
from books.models import Book

@login_required
def toggle_favorite(request, book_id):
  book = get_object_or_404(Book, id=book_id)
  fav, created = Favorite.objects.get_or_create(user=request.user, book=book)
  if not created:
    fav.delete()  # unfavorite if already exists
  return redirect('dashboard')  # or wherever you want to go back

@login_required
def favorite_books_view(request):
  # Get all favorite books of the current user
  favorites = Favorite.objects.filter(user=request.user).select_related('book')
  favorite_books = [fav.book for fav in favorites]
  
  context = { 'favorite_books': favorite_books }
  return render(request, 'favorites/index.html', context)

# C:\Users\v-deepak.sharma\Desktop\BOOK\venv\my_book\templates\favorites\index.html
