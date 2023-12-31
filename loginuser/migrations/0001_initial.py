# Generated by Django 4.2.6 on 2023-10-18 06:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo_url', models.CharField(blank=True, max_length=256, verbose_name='Ссылка на фото')),
                ('image', models.ImageField(blank=True, upload_to='userprofile/image', verbose_name='Изображение')),
                ('firstname', models.CharField(blank=True, max_length=25, verbose_name='Имя')),
                ('lastname', models.CharField(blank=True, max_length=25, verbose_name='Фамилия')),
                ('birth', models.DateField(blank=True, verbose_name='Дата рождения')),
                ('e_mail', models.CharField(blank=True, max_length=25, verbose_name='Почта')),
                ('phone', models.BigIntegerField(blank=True, verbose_name='Телефон')),
                ('social_vk', models.CharField(blank=True, max_length=25, verbose_name='Вконтакте')),
                ('social_ok', models.CharField(blank=True, max_length=25, verbose_name='Одноклассники')),
                ('social_inst', models.CharField(blank=True, max_length=25, verbose_name='Инста')),
                ('social_tube', models.CharField(blank=True, max_length=25, verbose_name='Видео')),
                ('username', models.CharField(blank=True, max_length=25, verbose_name='Логин')),
                ('password', models.CharField(blank=True, max_length=25, verbose_name='Пароль')),
                ('about', models.TextField(blank=True, verbose_name='Описание')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'userprofile',
                'verbose_name_plural': 'Профиль',
            },
        ),
    ]
