from django.urls import path

from . import views

app_name = "encyclopedia"

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.entry, name="entry"),
    path("wiki/", views.random_entry, name="random_page"),
    path("search/", views.search, name="search_page"),
    path("new/", views.new_entry, name="new_entry")
]
