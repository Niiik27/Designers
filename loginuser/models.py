from django.contrib.auth.models import User
from django.db import models
# from django.contrib.auth.models import User
from APP_NAMES import APP_NAMES,VERBOSE_APP_NAMES
len_fields = 15
class UserProfile(models.Model):
    photo_url = models.CharField('Ссылка на фото',max_length=256, blank=True)
    image = models.ImageField('Изображение', upload_to=f'{APP_NAMES.USER_PROFILE}/image', blank=True)
    firstname = models.CharField('Имя', max_length=len_fields, blank=True)
    lastname = models.CharField('Фамилия', max_length=len_fields, blank=True)
    birth = models.DateField('Дата рождения', blank=True)
    e_mail = models.CharField('Почта', max_length=len_fields, blank=True)
    phone = models.BigIntegerField('Телефон', blank=True)
    sotial_vk = models.CharField('Вконтакте', max_length=len_fields, blank=True)
    sotial_ok = models.CharField('Одноклассники', max_length=len_fields, blank=True)
    sotial_inst = models.CharField('Инста', max_length=len_fields, blank=True)
    sotial_tube = models.CharField('Видео', max_length=len_fields, blank=True)
    username = models.CharField('Логин', max_length=len_fields, blank=True)
    password = models.CharField('Пароль', max_length=len_fields, blank=True)
    about = models.TextField('Описание', blank=True)
    # Внешний ключ
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    @staticmethod
    def create_user_profile(POST):
        d = dict(POST)
        userProfile = UserProfile()
        for key in d:

            if key != 'csrfmiddlewaretoken' and key!='image' and key!='birth':
                print(key,d[key])
                userProfile.__setattr__(key,d[key])
        # userProfile = cls(photo_url=POST['photo_url'],image=POST['image'],firstname=POST['firstname'],lastname=POST['lastname'],birth=POST['birth'],e_mail=POST['e_mail'],phone=POST['phone'],sotial_vk=POST['sotial_vk'],sotial_ok=POST['sotial_ok'],sotial_inst=POST['sotial_inst'],sotial_tube=POST['sotial_tube'],username=POST['username'],password=POST['password'],about=POST['about'],user=POST['user'])

        userProfile.save()
        return userProfile
    def __str__(self):
        return f"{self.username} | {self.firstname} {self.lastname} | {self.birth}"
    class Meta:
        verbose_name = APP_NAMES.USER_PROFILE
        verbose_name_plural = VERBOSE_APP_NAMES.USER_PROFILE


