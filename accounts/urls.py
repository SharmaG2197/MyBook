from django.urls import path
from .views import dashboard, signup_view, login_view, logout_view

urlpatterns = [
    path('', dashboard, name='dashboard'),  # Dashboard as home page
    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
]