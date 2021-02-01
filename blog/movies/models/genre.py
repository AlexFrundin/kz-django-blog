from django.db import models as m


class Genre(m.Model):
    genre = m.CharField(verbose_name="Жанр", max_length=20, unique=True)

    class Meta:
        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"
        ordering = ('-genre',)

    def __str__(self):
        return self.genre
