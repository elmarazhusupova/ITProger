# Generated by Django 4.0.2 on 2022-02-28 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='articles',
            options={'verbose_name': 'Новость', 'verbose_name_plural': 'Новости'},
        ),
        migrations.AddField(
            model_name='articles',
            name='anons',
            field=models.CharField(default='None', max_length=250, verbose_name='Anons'),
        ),
        migrations.AddField(
            model_name='articles',
            name='full_text',
            field=models.TextField(default='News', verbose_name='Statya'),
        ),
        migrations.AddField(
            model_name='articles',
            name='title',
            field=models.CharField(default='News', max_length=50, verbose_name='Name'),
        ),
    ]
