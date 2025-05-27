from django.urls import path
from . import views

urlpatterns = [
  path('books/<int:book_id>/rate/', views.create_rating, name='create_rating'),
  path('rating/<int:rating_id>/delete/', views.delete_rating, name='delete_rating'),
]


# C:\Users\v-deepak.sharma\Desktop\BOOK\venv\my_book\book_rating\urls.py