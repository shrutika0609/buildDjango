from django.urls import path
from . import views  # Import the views from the current directory

urlpatterns = [
    path('hello/', views.hello_world, name='hello_world'),
    path('homepage/', views.homepage, name='homepage'),
    path('display-date/', views.display_date, name='display_date'),
    path('menu/', views.menu, name='menu'),
]
