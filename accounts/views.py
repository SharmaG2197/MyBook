from datetime import datetime
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from .forms import SignupForm, LoginForm
from .middlewares import auth, guest
from .models import Account
from books.models import Book
from favorites.models import Favorite


@auth
def dashboard(request):
  # Get all books owned by current user
  books = Book.objects.exclude(user=request.user).order_by('-id')

  # Get all favorite book ids for current user
  favorite_books = Favorite.objects.filter(user=request.user).values_list('book_id', flat=True)
  
  return render(request, 'dashboard/index.html',
                { 'year': datetime.now().year, 'books': books, 'user_favorites': favorite_books })


@guest
def signup_view(request):
  if request.method == 'POST':
    form = SignupForm(request.POST)
    if form.is_valid():
      account = form.save()
      login(request, account)
      return redirect('login')
    else:
      return render(request, 'accounts/signup.html', {'form': form})

  else:
    initial_data = {'email': '', 'password1': '', 'password2': '', 'termsandconditions_and_privacy_policy': '', 'marketing_mail': ''}
    form = SignupForm(initial=initial_data)
    return render(request, 'accounts/signup.html', {'form': form})


@guest
def login_view(request):
  if request.method == 'POST':
    form = AuthenticationForm(request, data=request.POST)
    if form.is_valid():
      account = form.get_user()
      login(request, account)
      return redirect('dashboard')
    else:
      return render(request, 'accounts/login.html', {'form': form})
  else:
    form = LoginForm()
    return render(request, 'accounts/login.html', {'form': form})


def logout_view(request):
  logout(request)
  return redirect('login')


# C:\Users\v-deepak.sharma\Desktop\BOOK\venv\my_book\accounts\views.py
