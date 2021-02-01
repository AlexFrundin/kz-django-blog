from django.db import models as m
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.contenttypes.fields import GenericRelation
from django.urls import reverse
from django.utils.safestring import mark_safe


class IntervalField(m.PositiveSmallIntegerField):
    def __init__(self, verbose_name=None, min_value=None,
                 max_value=None, **kwargs):
        self.min_value, self.max_value = min_value, max_value
        m.PositiveSmallIntegerField.__init__(self, verbose_name, **kwargs)

    def formfield(self, **kwargs):
        defaults = {"min_value": self.min_value, "max_value": self.max_value}
        defaults.update(**kwargs)
        return super(IntervalField, self).formfield(**defaults)


class Movie(m.Model):

    title = m.CharField(verbose_name='Название', max_length=20)
    year = m.PositiveSmallIntegerField(
        verbose_name='Год выпуска',
        validators=[MinValueValidator(1900, message="Вы спорите с историей?"),
                    MaxValueValidator(2021, message="Вы из будущего?")]
    )

    actors = m.ManyToManyField('Actor', related_name='movies')
    genres = m.ManyToManyField('Genre', related_name='movies')
    images = GenericRelation('Image', related_query_name='movies')

    # images

    class Meta:
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'
        constraints = (m.UniqueConstraint(
            fields=['title', 'year'],
            name="unique_movie"),)

    def __str__(self):
        return f'title={self.title} year={self.year}'

    def get_actors(self):
        actors = self.actors.values_list('first_name', 'second_name')
        return ", ".join((" ".join(actor) for actor in actors))

    def get_genres(self):
        genres = self.genres.values_list('genre', flat=True)
        return ", ".join(genres)

    get_actors.short_description = 'Актеры'
    get_actors.short_description = 'Жанры'

    def get_absolute_url(self):
        return reverse('movie_get', kwargs={'pk': self.id})

    def get_delete_url(self):
        return reverse('movie_delete', kwargs={'pk': self.id})

    def preview(self):
        img = self.images.first()
        if img:
            return mark_safe(f'<img width="30" height="30" src="{img.image.url}">')
        return mark_safe(f'<img width="30" height="30" src="/media/default.jpg">')
