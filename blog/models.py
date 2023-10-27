from django.db import models
from APP_NAMES import APP_NAMES,VERBOSE_APP_NAMES

class Article(models.Model):
    title = models.CharField('Заголовок',max_length=15)  # Ограниченная строка
    desc= models.TextField('Описание')  # Ограниченная строка
    image= models.ImageField('Изображение',upload_to=f'{APP_NAMES.BLOG}/image')  # строка по изображению (отдельный тип данных)
    date = models.DateField('Дата')  # Дата
    url = models.URLField('Доп. источник',blank=True)  # Ссылка
    def __str__(self):
        return f"{self.title} | {self.date}"
    class Meta:
        verbose_name = APP_NAMES.ARTICLES
        verbose_name_plural = VERBOSE_APP_NAMES.ARTICLES
