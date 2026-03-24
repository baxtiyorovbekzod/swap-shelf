from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend

from .models import Book, Genre, BookStatus
from .serializers import BookSerializer, GenreSerializer
from .permissions import IsOwnerOrReadOnly
from .utils import send_to_telegram

# 📚 Book Shelf: list + create
class BookListCreateView(generics.ListCreateAPIView):
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return Book.objects.select_related("owner", "genre").all()

    def perform_create(self, serializer):
        book = serializer.save(owner=self.request.user)
        if book.share:
            send_to_telegram(book)

# 📖 Detail: update / delete
class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.select_related("owner", "genre")
    serializer_class = BookSerializer
    permission_classes = [IsOwnerOrReadOnly]

# 🔎 Browse: only available books
class BookBrowseView(generics.ListAPIView):
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ["genre", "condition", "type"]
    search_fields = ["title", "author"]

    def get_queryset(self):
        return Book.objects.select_related("owner", "genre").filter(
            status=BookStatus.AVAILABLE
        )

# 👤 My Books
class MyBooksView(generics.ListAPIView):
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Book.objects.filter(owner=self.request.user)

# 📂 Genres list
class GenreListView(generics.ListAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer