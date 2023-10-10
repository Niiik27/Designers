from django.db import models
from django.contrib.auth.models import User
from APP_NAMES import APP_NAMES, VERBOSE_APP_NAMES


class Artwork(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    title = models.CharField('Название',max_length=50)  # Ограниченная строка
    desc= models.TextField('Описание')  # Ограниченная строка
    image= models.ImageField('Изображение', upload_to=f'{APP_NAMES.PORTFOLIO}/image')  #  строка по изображению (отдельный тип данных)
    date = models.DateField('Дата')  # Дата
    url = models.URLField('В сотрудничестве',blank=True)  # Ссылок может быть много, пока не знаю как лучше сохранить ссылки на коллег и партнеров, возможно нужен список

    def __str__(self):
        return f"{self.title} | {self.date}"
    class Meta:
        verbose_name = APP_NAMES.PORTFOLIO
        verbose_name_plural = VERBOSE_APP_NAMES.PORTFOLIO

