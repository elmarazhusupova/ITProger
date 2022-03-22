from django.db import models


class Articles(models.Model):
    title = models.CharField('Name', max_length=50, default='News')
    anons = models.CharField('Anons', max_length=250, default='None')
    full_text = models.TextField('Statya', default='News')
    date = models.DateTimeField('Data of published')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
