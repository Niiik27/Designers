from django.db import models
# from .views import app_name, verbose_app_name


# Таблица мероприятий
class MyEvent(models.Model):
    pass
    # title = models.CharField(verbose_name='Заголовок', max_length=15)  # Ограниченная строка
    # desc = models.TextField(verbose_name='Описание')  # Ограниченная строка
    # image = models.ImageField(verbose_name='Изображение', upload_to='blog/image')  # строка по изображению (отдельный тип данных)
    # date = models.DateField(verbose_name='Дата')  # Дата
    # url = models.URLField('Подробнее о событии', blank=True)  # Ссылка
    # class Meta:
    #     verbose_name = app_name
    #     verbose_name_plural = verbose_app_name
    # def __str__(self):
    #     return f"{self.title} | {self.date}"


