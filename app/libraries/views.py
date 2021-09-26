from rest_framework.viewsets import ModelViewSet

from libraries.models import Libraries, Bookshelves, Books
from libraries.serializers import (
    LibrariesSerializer,
    BookshelvesSerializer,
    BooksSerializer,
    BookshelvesCreateSerializer,
    BooksCreateSerializer,
)


class LibrariesViewSet(ModelViewSet):
    serializer_class = LibrariesSerializer
    queryset = Libraries.objects.all()


class BookshelvesViewSet(ModelViewSet):
    queryset = Bookshelves.objects.all()

    def get_serializer_class(self):
        if self.action in ("create", "update", "partial_update"):
            return BookshelvesCreateSerializer
        return BookshelvesSerializer


class BooksViewSet(ModelViewSet):
    queryset = Books.objects.all()

    def get_serializer_class(self):
        if self.action in ("create", "update", "partial_update"):
            return BooksCreateSerializer
        return BooksSerializer
