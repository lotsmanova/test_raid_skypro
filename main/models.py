from django.db import models


class FrameworkModel(models.Model):
    name = models.CharField(max_length=200, verbose_name='название')
    language = models.CharField(max_length=200, verbose_name='язык программирования')

    def __str__(self):
        return f'{self.name} - {self.language}'

    class Meta:
        verbose_name = 'фреймворк'
        verbose_name_plural = 'фреймворки'
