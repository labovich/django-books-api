from rest_framework import routers

from libraries.views import LibrariesViewSet, BookshelvesViewSet, BooksViewSet

libraries_router = routers.DefaultRouter()
libraries_router.register(r"libraries", LibrariesViewSet, "libraries")
libraries_router.register(r"bookshelves", BookshelvesViewSet, "bookshelves")
libraries_router.register(r"books", BooksViewSet, "books")
