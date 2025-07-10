from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"), # This is the page that contains the urls belonging to wiki/
    path("wiki/<str:title>", views.entry, name = "entry"), # This applies to any title that you give after wiki/ which calls the entry method in views, which calls the html template created for entry
    path("search", views.search, name = "search"),
    path("new", views.new_page, name = "new_page"),
    path("wiki/<str:title>/edit", views.edit_page, name = "edit_page"),
    path("random", views.random_page, name = "random_page")
]
