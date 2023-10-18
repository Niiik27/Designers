import os

from django.db.models.signals import pre_delete

from django.db import models
from django.contrib.auth.models import User
from APP_NAMES import APP_NAMES, VERBOSE_APP_NAMES

def user_directory_path(instance, filename):
    user_id = instance.user.id
    username = instance.user.username
    return f'{APP_NAMES.PORTFOLIO}/user_{username}_{user_id}/{filename}'
def thumb_directory_path(instance, filename):
    user_id = instance.user.id
    username = instance.user.username
    return f'{APP_NAMES.PORTFOLIO}/user_{username}_{user_id}/tmb/{filename}'
class Artwork(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField('Название',max_length=50)
    image= models.ImageField('Изображение', upload_to=user_directory_path)
    thumb = models.ImageField('Миниатюра', upload_to=thumb_directory_path)
    desc = models.TextField('Описание', blank=True)
    date = models.DateField('Дата',blank=True)  # Дата
    url = models.URLField('В сотрудничестве',blank=True)

    def __str__(self):
        return f"{self.title} | {self.date}"

    def delete(self, *args, **kwargs):
        self.image.delete()
        self.thumb.delete()
        super().delete(*args, **kwargs)

    class Meta:
        verbose_name = APP_NAMES.PORTFOLIO
        verbose_name_plural = VERBOSE_APP_NAMES.PORTFOLIO



