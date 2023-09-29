from django.db import models
from APP_NAMES import APP_NAMES, VERBOSE_APP_NAMES


# Таблица мероприятий
class Event(models.Model):
    title = models.CharField(verbose_name='Заголовок', max_length=15)  # Ограниченная строка
    desc = models.TextField(verbose_name='Описание')  # Ограниченная строка
    image = models.ImageField(verbose_name='Изображение', upload_to='blog/image')  # строка по изображению (отдельный тип данных)
    date = models.DateField(verbose_name='Дата')  # Дата
    url = models.URLField('Подробнее о событии', blank=True)  # Ссылка
    class Meta:
        verbose_name = APP_NAMES.EVENTS
        verbose_name_plural = VERBOSE_APP_NAMES.EVENTS

    def __str__(self):
        return f"{self.title} | {self.date}"


