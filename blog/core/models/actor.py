from django.db import models as m


class Actor(m.Model):
    first_name = m.CharField(verbose_name="Имя", max_length=20)
    second_name = m.CharField(verbose_name="Фамилия", max_length=20)
    birth = m.DateField(verbose_name="Дата рождения", blank=True, null=True)

    class Meta:
        verbose_name = "Актер"
        verbose_name_plural = "Актеры"
        constraints = ((m.UniqueConstraint(
            fields=["first_name", "second_name"],
            name="actor_unique"
        )),)

        ordering = ("-birth", "first_name")

    def __str__(self):
        return f'{self.first_name} {self.second_name}'
