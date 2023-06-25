from django.db import models


class Catalog(models.Model):
    title = models.CharField(max_length=200, verbose_name="Маркировка двери")
    image = models.ImageField(upload_to='image', verbose_name="Изоброжение")
    description = models.TextField(verbose_name="Описание")
    materials = models.TextField(verbose_name="Материалы", blank=True)
    equipment = models.TextField(verbose_name="Комлектация",blank=True)
    addition = models.TextField(verbose_name="Дополнительные опции", blank=True)
    permitted_size = models.TextField(verbose_name="Допустимые размеры", blank=True)

    def __str__(self):
        return self.title;




