from django.db import models
from django.contrib.auth.models import User
from APP_NAMES import APP_NAMES,VERBOSE_APP_NAMES
len_fields = 15
class UserProfile(models.Model):
    len_fields = 15
    photo_url = models.CharField('Ссылка на фото',max_length=256)
    image = models.ImageField('Изображение', upload_to=f'{APP_NAMES.USER_PROFILE}/image')
    firstname = models.CharField('Имя', max_length=len_fields)
    lastname = models.CharField('Фамилия', max_length=len_fields)
    birth = models.DateField('Дата рождения')
    e_mail = models.CharField('Почта', max_length=len_fields)
    phone = models.IntegerField('Телефон')
    sotial_vk = models.CharField('Вконтакте', max_length=len_fields)
    sotial_ok = models.CharField('Одноклассники', max_length=len_fields)
    sotial_inst = models.CharField('Инста', max_length=len_fields)
    sotial_tube = models.CharField('Видео', max_length=len_fields)
    username = models.CharField('Логин', max_length=len_fields)
    password = models.CharField('Пароль', max_length=len_fields)
    about = models.TextField('Описание')
    def __str__(self):
        return f"{self.username} | {self.firstname} {self.lastname} | {self.birth}"
    class Meta:
        verbose_name = APP_NAMES.USER_PROFILE
        verbose_name_plural = VERBOSE_APP_NAMES.USER_PROFILE


def create_user_profile(sender,instance, created,**kwargs):
    if created:
        UserProfile.objects.create(user=instance)

def save_user_profile(sender,instance,**kwargs):
    instance.userprofile.save()