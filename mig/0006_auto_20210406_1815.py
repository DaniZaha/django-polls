# Generated by Django 3.1.7 on 2021-04-06 15:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('polls', '0005_auto_20210406_1812'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='article_author',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='article_author_user', to=settings.AUTH_USER_MODEL),
        ),
    ]
