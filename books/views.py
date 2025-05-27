from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Book
from .forms import BookForm
from django.db.models import Avg
from collections import Counter


@login_required
def index(request):
  books = Book.objects.filter(user=request.user)
  return render(request, 'books/index.html', {'books': books})


def show(request, pk):
  book = get_object_or_404(Book, id=pk)

  ratings = book.ratings.all()
  average_rating = ratings.aggregate(Avg('rating'))['rating__avg'] or 0
  average_rating = round(average_rating, 1)
  total_reviews = ratings.count()

  rating_counts = Counter(rating.rating for rating in ratings)

  rating_stats = []
  for star in range(5, 0, -1):
    count = rating_counts.get(star, 0)
    percentage = (count / total_reviews) * 100 if total_reviews > 0 else 0

    # ❗ Calculate width out of 5 (i.e., for 3-star = 60%)
    bar_width = (star / 5) * 100
    rating_stats.append({ 'star': star, 'count': count, 'percentage': round(percentage), 'bar_width': round(bar_width) })

  context = { "book": book, "average_rating": average_rating, "total_reviews": total_reviews, "rating_stats": rating_stats }

  return render(request, "books/show.html", context)




# def show(request, pk):
#     book = get_object_or_404(Book, pk=pk)
#     return render(request, 'books/show.html', {'book': book})


@login_required
def create(request):
  if request.method == 'POST':
    form = BookForm(request.POST, request.FILES)
    if form.is_valid():
      book = form.save(commit=False)  
      book.user = request.user
      book.save()
      return redirect('show', pk=book.pk)
  else:
    form = BookForm()
  return render(request, 'books/form.html', {'form': form})


@login_required
def update(request, pk):
  book = get_object_or_404(Book, pk=pk)
  if book.user != request.user:
    return redirect('show', pk=pk)
  form = BookForm(request.POST or None, request.FILES or None, instance=book)
  if form.is_valid():
    form.save()
    return redirect('show', pk=pk)
  return render(request, 'books/form.html', {'form': form})


@login_required
def delete(request, pk):
  book = get_object_or_404(Book, pk=pk)
  if book.user == request.user:
    book.delete()
  return redirect('index')
