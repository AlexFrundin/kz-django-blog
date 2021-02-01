from django.db import models as m
from django.contrib.contenttypes.fields import GenericRelation
from django.utils.safestring import mark_safe
from django.urls import reverse

class Actor(m.Model):
    first_name = m.CharField(verbose_name="Имя", max_length=20)
    second_name = m.CharField(verbose_name="Фамилия", max_length=20)
    birth = m.DateField(verbose_name="Дата рождения", blank=True, null=True)

    images = GenericRelation('Image', related_query_name='actors')

    class Meta:
        verbose_name = "Актер"
        verbose_name_plural = "Актеры"
        constraints = ((m.UniqueConstraint(
            fields=["first_name", "second_name"],
            name="unique_actor"
        )),)

        ordering = ("-birth", "first_name")

    def __str__(self):
        return f'{self.first_name} {self.second_name}'

    def preview(self):
        img = self.images.first()
        return mark_safe(f'<img width="30" height="30" src="{img.image.url}">')

    def get_absolute_url(self):
        return  reverse('actor_get', kwargs={'pk': self.id})
