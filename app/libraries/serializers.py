from rest_framework import serializers
from rest_framework.fields import IntegerField
from rest_framework.serializers import ModelSerializer

from libraries.models import Libraries, Bookshelves, Books


class LibrariesBaseSerializer(ModelSerializer):
    class Meta:
        model = Libraries
        fields = ("id", "name")
        read_only_fields = ("id", "name")


class LibrariesSerializer(LibrariesBaseSerializer):
    class Meta(LibrariesBaseSerializer.Meta):
        fields = "__all__"
        read_only_fields = ("id", "created", "updated")


class BookshelvesBaseSerializer(ModelSerializer):
    class Meta:
        model = Bookshelves
        fields = ("id", "number")


class BookshelvesCreateSerializer(BookshelvesBaseSerializer):
    library_id = IntegerField(required=True)
    number = IntegerField(required=True, min_value=1)

    class Meta(BookshelvesBaseSerializer.Meta):
        fields = ("number", "library_id", "id", "created", "updated")
        read_only_fields = ("id", "created", "updated")

    def validate_library_id(self, value):
        if not Libraries.objects.filter(id=value).exists():
            raise serializers.ValidationError("Invalid library_id.")
        return value


class BookshelvesSerializer(BookshelvesBaseSerializer):
    library = LibrariesBaseSerializer()

    class Meta(BookshelvesBaseSerializer.Meta):
        fields = "__all__"
        read_only_fields = ("id", "library", "created", "updated")


class BooksBaseSerializer(ModelSerializer):
    class Meta:
        model = Books
        fields = ("name", "author", "year")


class BooksCreateSerializer(BooksBaseSerializer):
    bookshelf_id = IntegerField(required=True)
    year = IntegerField(required=True, min_value=1900, max_value=2100)

    class Meta(BooksBaseSerializer.Meta):
        fields = ("name", "author", "year", "bookshelf_id", "id", "created", "updated")
        read_only_fields = ("id", "bookshelf", "created", "updated")

    def validate_bookshelf_id(self, value):
        if not Bookshelves.objects.filter(id=value).exists():
            raise serializers.ValidationError("Invalid bookshelf_id.")
        return value


class BooksSerializer(BooksBaseSerializer):
    bookshelf = BookshelvesBaseSerializer()

    class Meta(BooksBaseSerializer.Meta):
        model = Books
        fields = "__all__"
        read_only_fields = ("id", "bookshelf", "created", "updated")
