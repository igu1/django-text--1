from django.contrib import admin
from django.urls import path
from .views import index, home

urlpatterns = [
    path("", home, name='home'),
    path('<int:id>', index, name='home2')
]
