from django.contrib import admin

# Register your models here.
from libraries.models import Libraries, Bookshelves, Books

admin.site.register(Libraries)
admin.site.register(Bookshelves)
admin.site.register(Books)
