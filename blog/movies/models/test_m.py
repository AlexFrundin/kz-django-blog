from django.db import models as m


class TestModel(m.Model):
    actor_id = m.ForeignKey('Actor', related_name='test', on_delete=m.CASCADE)
    genre_id = m.ForeignKey('Genre', related_name='test', on_delete=m.CASCADE)
