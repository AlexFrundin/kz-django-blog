from django.db import models as m
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType


class Image(m.Model):
    alt_extra = m.CharField(verbose_name="Описание для робота",
                            max_length=20, blank=True, null=True)
    image = m.ImageField(default='default.jpg')
    # first = m.BooleanField(verbose_name="Главное фото", default=False)

    content_type = m.ForeignKey(ContentType, on_delete=m.CASCADE)
    object_id = m.PositiveSmallIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
