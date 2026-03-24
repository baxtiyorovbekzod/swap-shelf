from rest_framework import serializers
from .models import Book, Genre

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = "__all__"

class BookSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.username")
    genre_name = serializers.ReadOnlyField(source="genre.name")

    class Meta:
        model = Book
        fields = "__all__"