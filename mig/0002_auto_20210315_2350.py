# Generated by Django 3.1.7 on 2021-03-15 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='dislikes',
            field=models.IntegerField(default=0, verbose_name='dislikes'),
        ),
        migrations.AddField(
            model_name='article',
            name='likes',
            field=models.IntegerField(default=0, verbose_name='likes'),
        ),
    ]
