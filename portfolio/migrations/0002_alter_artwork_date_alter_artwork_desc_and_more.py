# Generated by Django 4.2.6 on 2023-10-14 11:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import portfolio.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artwork',
            name='date',
            field=models.DateField(blank=True, verbose_name='Дата'),
        ),
        migrations.AlterField(
            model_name='artwork',
            name='desc',
            field=models.TextField(blank=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='artwork',
            name='image',
            field=models.ImageField(upload_to=portfolio.models.user_directory_path, verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='artwork',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]