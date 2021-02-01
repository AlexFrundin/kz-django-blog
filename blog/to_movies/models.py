from django.db import models


class Actor(models.Model):
    id = models.AutoField()
    name = models.CharField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'actor'


class ActorMovie(models.Model):
    id = models.AutoField()
    movie = models.ForeignKey('Movie', models.DO_NOTHING)
    actor = models.ForeignKey(Actor, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'actor_movie'


class Genre(models.Model):
    id = models.AutoField()
    name = models.CharField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'genre'


class GenreMovie(models.Model):
    genre = models.ForeignKey(Genre, models.DO_NOTHING)
    movie = models.ForeignKey('Movie', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'genre_movie'


class Movie(models.Model):
    id = models.AutoField()
    title = models.CharField(blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'movie'
