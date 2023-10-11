from django.db import models
from django.contrib.auth.models import User
from APP_NAMES import APP_NAMES, VERBOSE_APP_NAMES

def user_directory_path(instance, filename):
    # Переменная `instance` содержит текущий объект модели
    # Получаем id пользователя (user_id)
    user_id = instance.user.id
    # Или получаем имя пользователя (username)
    username = instance.user.username
    # Возвращаем путь сохранения файла
    return f'{APP_NAMES.PORTFOLIO}/user_{username}_{user_id}/{filename}'  # Или f'{username}/{filename}'
class Artwork(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    title = models.CharField('Название',max_length=50)  # Ограниченная строка
    desc= models.TextField('Описание')  # Ограниченная строка
    image= models.ImageField('Изображение', upload_to=user_directory_path)  #  строка по изображению (отдельный тип данных)
    date = models.DateField('Дата')  # Дата
    url = models.URLField('В сотрудничестве',blank=True)  # Ссылок может быть много, пока не знаю как лучше сохранить ссылки на коллег и партнеров, возможно нужен список

    def __str__(self):
        return f"{self.title} | {self.date}"
    class Meta:
        verbose_name = APP_NAMES.PORTFOLIO
        verbose_name_plural = VERBOSE_APP_NAMES.PORTFOLIO

