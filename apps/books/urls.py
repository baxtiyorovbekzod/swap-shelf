from django.urls import path
from .views import (
    BookListCreateView,
    BookDetailView,
    BookBrowseView,
    GenreListView,
    MyBooksView,
)

urlpatterns = [
    path("", BookListCreateView.as_view()),
    path("browse/", BookBrowseView.as_view()),
    path("my/", MyBooksView.as_view()),
    path("<int:pk>/", BookDetailView.as_view()),
    path("genres/", GenreListView.as_view()),
]