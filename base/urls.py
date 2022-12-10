from django.contrib import admin
from django.urls import path
from .views import index, home, delete_blog

urlpatterns = [
    path("", home, name='home'),
    path('<int:id>', index, name='home2'),
    path('<int:id>/delete', delete_blog, name='blog-delete')
]
