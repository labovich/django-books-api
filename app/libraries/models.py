from django.db import models


# Create your models here.


class BaseModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Libraries(BaseModel):
    name = models.CharField(max_length=255, blank=False, null=False, unique=True)
    address = models.TextField(blank=False, null=False)

    def __str__(self):
        return f"Library: {self.name}"

    class Meta:
        ordering = ["-created"]
        verbose_name = "Library"
        verbose_name_plural = "Libraries"


class Bookshelves(BaseModel):
    library = models.ForeignKey(
        Libraries, related_name="bookshelves", null=False, on_delete=models.CASCADE
    )
    number = models.PositiveIntegerField(blank=False, null=False)

    def __str__(self):
        return f"Bookshelf: {self.library.name} - {self.number}"

    class Meta:
        ordering = ["library__name", "number"]
        unique_together = [["library", "number"]]
        verbose_name = "Bookshelf"
        verbose_name_plural = "Bookshelves"


class Books(BaseModel):
    name = models.CharField(max_length=255, blank=False, null=False, unique=True)
    author = models.CharField(max_length=255, blank=False, null=False, unique=True)
    year = models.PositiveSmallIntegerField(blank=False, null=False)
    bookshelf = models.ForeignKey(
        Bookshelves, related_name="books", null=False, on_delete=models.CASCADE
    )

    def __str__(self):
        return f"Book: {self.name} - {self.author}"

    class Meta:
        ordering = ["name"]
        verbose_name = "Book"
        verbose_name_plural = "Books"
