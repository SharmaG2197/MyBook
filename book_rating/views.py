from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.db import models
from .forms import RatingForm
from .models import BookRating
from books.models import Book


# @login_required
# def create_rating(request, book_id):
#   book = get_object_or_404(Book, id=book_id)

#   if request.method == "POST":
#     form = RatingForm(request.POST)
#     if form.is_valid():
#       rating, created = BookRating.objects.update_or_create(user=request.user, book=book, 
#                                                             defaults={ "rating": form.cleaned_data["rating"],
#                                                                        "comment": form.cleaned_data["comment"] })

#       messages.success(request, "Your rating has been submitted!")
#       return redirect("show", pk=book.id)
#   else:
#     form = RatingForm()
#     context = { "book": book, "form": form }
#     return render(request, "book_rating/rate_book.html", context)

@login_required
def create_rating(request, book_id):
    book = get_object_or_404(Book, id=book_id)

    if request.method == "POST":
        form = RatingForm(request.POST)
        if form.is_valid():
            # Check if user already rated this book
            if BookRating.objects.filter(user=request.user, book=book).exists():
                messages.warning(request, "You have already rated this book.")
                context = { "book": book, "form": form }
                return render(request, "book_rating/rate_book.html", context)

            # Create new rating
            BookRating.objects.create(
                user=request.user,
                book=book,
                rating=form.cleaned_data["rating"],
                comment=form.cleaned_data["comment"]
            )
            messages.success(request, "Your rating has been submitted!")
            return redirect("show", pk=book.id)
    else:
        form = RatingForm()

    context = { "book": book, "form": form }
    return render(request, "book_rating/rate_book.html", context)

@login_required
def delete_rating(request, rating_id):
  rating = get_object_or_404(BookRating, id=rating_id, user=request.user)
  book_id = rating.book.id
  rating.delete()
  messages.success(request, "Your rating has been removed.")
  return redirect("book_detail", book_id=book_id)


# C:\Users\v-deepak.sharma\Desktop\BOOK\venv\my_book\book_rating\views.py