# Generated by Django 3.1.7 on 2021-04-06 15:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('polls', '0004_article_article_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='article_author',
            field=models.ForeignKey(blank=True, default='anonymus user', on_delete=django.db.models.deletion.SET_DEFAULT, related_name='article_author_user', to=settings.AUTH_USER_MODEL),
        ),
    ]
