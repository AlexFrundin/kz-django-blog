from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline
from .models import Movie, Genre, Actor, Image


class ImageInline(GenericTabularInline):
    model = Image
    extra = 1


class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'year', 'get_actors', 'get_genres')
    list_filter = ('title', 'year')
    inlines = [ImageInline]


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    model = Genre


class ActorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'second_name', 'birth', 'preview')
    list_filter = ('second_name', 'birth')
    inlines = [ImageInline]


admin.site.register(Image)
admin.site.register(Movie, MovieAdmin)
admin.site.register(Actor, ActorAdmin)
