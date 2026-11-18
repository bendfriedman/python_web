from django.conf import settings
from django.db import models


class Album(models.Model):

    class Genre(models.TextChoices):
        ROCK = 'ROCK', 'Rock'
        POP = 'POP', 'Pop'
        JAZZ = 'JAZZ', 'Jazz'
        HIPHOP = 'HIPHOP', 'Hip-Hop'
        ELECTRONIC = 'ELEC', 'Electronic'
        CLASSICAL = 'CLASS', 'Classical'
        METAL = 'METAL', 'Metal'
        OTHER = 'OTHER', 'Other'

    title = models.CharField(max_length=100)

    artist = models.CharField(max_length=100)  # Künstler:in / Band

    description = models.TextField(blank=True)

    genre = models.CharField(
        max_length=6,
        choices=Genre,
    )

    user = models.ForeignKey(  # Ersteller
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='albums',
        related_query_name='album',
    )

    created_at = models.DateTimeField(auto_now_add=True)  # Erstellungs-Zeitstempel

    class Meta:
        ordering = ['title', 'artist']
        verbose_name = 'Album'
        verbose_name_plural = 'Albums'

    def __str__(self):
        return f'{self.title} ({self.artist})'

    def __repr__(self):
        return f'{self.title} / {self.artist} / {self.genre} ({self.get_genre_display()})'
