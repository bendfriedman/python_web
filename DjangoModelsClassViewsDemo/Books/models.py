from datetime import date

from django.conf import settings
from django.db import models


class Book(models.Model):

    class BookType(models.TextChoices):
        HARDCOVER = 'H', 'Hardcover'
        PAPERBACK = 'P', 'Paperback'
        EBOOK = 'E', 'E-Book'
        AUDIOBOOK = 'A', 'Audio-Book'


    title = models.CharField(max_length=100)

    subtitle = models.CharField(
        max_length=100,
        blank=True)

    author = models.CharField(max_length=50)

    pages = models.IntegerField()  # Es ist ein Funktionsaufruf nötig, auch wenn es keine 'Einstellungen' gibt

    date_published = models.DateField(
        blank=True,
        default=date.today
    )

    type = models.CharField(
        max_length=1,
        choices=BookType,
    )

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='books',  # Rückbezug vom User Model auf das Books model (user.books.all())
        related_query_name='book',  # Rückbezug vom User Model auf das Books model (User.objects.filter(book__author="Newton"))
    )

    class Meta:
        ordering = ['title', '-type']
        verbose_name = 'Book'
        verbose_name_plural = 'Books'

    def get_full_title(self):

        if self.subtitle:  # if subtitle is not empty
            return f'{self.title}: {self.subtitle}'

        return self.title


    def __str__(self):
        return f'{self.title} ({self.author})'

    def __repr__(self):
        return f'{self.get_full_title()} / {self.author} / {self.type} ({self.get_type_display()})'
