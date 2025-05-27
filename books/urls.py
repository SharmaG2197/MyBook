from django.urls import path
from . import views

urlpatterns = [
  path('books', views.index, name='books_index'),
  path('books/<int:pk>/', views.show, name='show'),
  path('books/create/', views.create, name='create'),
  path('books/<int:pk>/edit/', views.update, name='update'),
  path('books/<int:pk>/delete/', views.delete, name='delete'),
]

# C:\Users\v-deepak.sharma\Desktop\BOOK\venv\my_book\books\urls.py