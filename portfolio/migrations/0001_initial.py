# Generated by Django 4.2.6 on 2023-10-18 06:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import portfolio.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Artwork',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Название')),
                ('image', models.ImageField(upload_to=portfolio.models.user_directory_path, verbose_name='Изображение')),
                ('thumb', models.ImageField(upload_to=portfolio.models.thumb_directory_path, verbose_name='Миниатюра')),
                ('desc', models.TextField(blank=True, verbose_name='Описание')),
                ('date', models.DateField(blank=True, verbose_name='Дата')),
                ('url', models.URLField(blank=True, verbose_name='В сотрудничестве')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'portfolio',
                'verbose_name_plural': 'Портфолио',
            },
        ),
    ]
