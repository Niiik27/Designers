from io import BytesIO
import requests
from PIL import Image
from django.contrib.auth.models import User
from django.core.files import File
from django.core.files.base import ContentFile
from django.core.files.uploadedfile import SimpleUploadedFile
from django.db import models
# from django.contrib.auth.models import User
from APP_NAMES import APP_NAMES,VERBOSE_APP_NAMES
from base64 import b64encode, b64decode
len_fields = 25
class UserProfile(models.Model):
    photo_url = models.CharField('Ссылка на фото',max_length=256, blank=True)
    image = models.ImageField('Изображение', upload_to=f'{APP_NAMES.USER_PROFILE}/image', blank=True)
    firstname = models.CharField('Имя', max_length=len_fields, blank=True)
    lastname = models.CharField('Фамилия', max_length=len_fields, blank=True)
    birth = models.DateField('Дата рождения', blank=True)
    e_mail = models.CharField('Почта', max_length=len_fields, blank=True)
    phone = models.BigIntegerField('Телефон', blank=True)
    social_vk = models.CharField('Вконтакте', max_length=len_fields, blank=True)
    social_ok = models.CharField('Одноклассники', max_length=len_fields, blank=True)
    social_inst = models.CharField('Инста', max_length=len_fields, blank=True)
    social_tube = models.CharField('Видео', max_length=len_fields, blank=True)
    username = models.CharField('Логин', max_length=len_fields, blank=True)
    password = models.CharField('Пароль', max_length=len_fields, blank=True)
    about = models.TextField('Описание', blank=True)
    # Внешний ключ
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def save_image_from_url(self, url):
        response = requests.get(url)
        if response.status_code == 200:
            img_data = BytesIO(response.content)
            img = Image.open(img_data)

            new_size = (300, 300)
            img.thumbnail(new_size)

            pathURL = url.split("?")[0]
            imgExt = pathURL[pathURL.rfind('.') + 1:len(pathURL)]
            if imgExt.lower()=='jpg':
                imgExt = 'jpeg'
            filename = pathURL.split('/')[-1]

            # Преобразуем изображение в байты
            buffer = BytesIO()
            img.save(buffer, format=imgExt)
            image_file = ContentFile(buffer.getvalue())

            # Сохраняем изображение в поле ImageField
            # self.image.save(filename, image_file)
            return image_file


    @staticmethod
    def create_user_profile(POST):
        d = dict(POST)
        userProfile = UserProfile()
        userProfile.photo_url = d.get('photo_url')[0]
        userProfile.image = userProfile.save_image_from_url(d.get('photo_url')[0])

        userProfile.firstname = d.get('firstname')[0]
        userProfile.lastname = d.get('lastname')[0]
        userProfile.birth = d.get('birth')[0]
        userProfile.e_mail = d.get('e_mail')[0]
        userProfile.phone = int(d.get('phone')[0])
        userProfile.social_vk = d.get('social_vk')[0]
        userProfile.social_ok = d.get('social_ok')[0]
        userProfile.social_inst = d.get('social_inst')[0]
        userProfile.social_tube = d.get('social_tube')[0]

        userProfile.username = d.get('username')[0]
        userProfile.password = d.get('password1')[0]
        userProfile.about = d.get('about')[0]






        return userProfile
    def __str__(self):
        return f"{self.username} | {self.firstname} {self.lastname} | {self.birth}"
    class Meta:
        verbose_name = APP_NAMES.USER_PROFILE
        verbose_name_plural = VERBOSE_APP_NAMES.USER_PROFILE


