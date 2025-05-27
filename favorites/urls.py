from django.urls import path
from . import views

urlpatterns = [
  path('favorites', views.favorite_books_view, name='favorites_index'),
  path('favorite/<int:book_id>/', views.toggle_favorite, name='toggle_favorite'),
]
