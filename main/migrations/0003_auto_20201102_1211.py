# Generated by Django 3.1.2 on 2020-11-02 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20201102_1210'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='datatime2',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Момент публикации'),
        ),
        migrations.AddField(
            model_name='question',
            name='title2',
            field=models.CharField(default='', max_length=255, verbose_name='Название'),
        ),
    ]
