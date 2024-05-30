from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("index.html", views.index, name='home'),
    path("about.html", views.about, name='about'),
    path("category.html", views.category, name='category'),
    path("work.html", views.work, name='work'),
]
