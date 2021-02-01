from django import forms
from django.contrib.contenttypes.models import ContentType

from .models import Movie, Image, Actor


class BaseForm(forms.ModelForm):
    images = forms.ImageField(label='Фотография', required=False)
    create = forms.BooleanField(label='Добавить фото', widget=forms.CheckboxInput, required=False)

    def save(self):
        cleaned_data = super().clean()
        image = cleaned_data.pop('images')
        create = cleaned_data.pop('create')
        obj = super().save(cleaned_data)
        if create:
            obj_type = ContentType.objects.get_for_model(obj)
            img = Image(image=image, object_id=obj.id, content_type=obj_type)
            img.save()
        return obj


class MovieForm(BaseForm):

    class Meta:
        model = Movie
        exclude = ['images']
        labels = {
            'title': 'Название фильма:',
            'year': 'Год выпуска:',
            'actors': 'Список актеров',
            'genres': 'Список жанров',
        }


class ActorForm(BaseForm):

    class Meta:
        model = Actor
        exclude = ['images']
        labels = {
            'first_name': 'Имя актера:',
            'last_name': 'Фамилия актера:',
            'birth': 'Год рождения',
        }
