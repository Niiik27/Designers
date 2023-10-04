import os
from base64 import b64encode
from pprint import pprint

from django.shortcuts import render
import requests
from io import BytesIO
from django.core.files import File
from PIL import Image
from APP_NAMES import APP_NAMES, VERBOSE_APP_NAMES

app_name = APP_NAMES.USER_PROFILE
verbose_name = VERBOSE_APP_NAMES.USER_PROFILE


def get_image(url):
    contestImgURL = url.split("?")[0]
    imgExt = contestImgURL[contestImgURL.rfind('.') + 1:len(contestImgURL)]
    response = requests.get(url, stream=True)
    content = response.content
    contestImgBase64 = b64encode(content).decode('utf-8')
    return imgExt, contestImgBase64

def save_image_from_url(url):
    response = requests.get(url)
    if response.status_code == 200:
        img_data = BytesIO(response.content)
        img = Image.open(img_data)
        img_path = 'images/your_image_name.jpg'  # Путь, по которому нужно сохранить изображение в папке media
        img.save(img_path)

        # Сохраняем изображение в модель
        model_instance = YourModel()
        with open(img_path, 'rb') as f:
            model_instance.image.save('your_image_name.jpg', File(f), save=True)
        # Удаляем временный файл
        os.remove(img_path)

def profileView(request):


    photo_url = request.GET.get('photo_url')
    img = get_image(photo_url)
    photo_img = img[1]
    photo_ext = img[0]
    pprint(photo_img)
    firstname = request.GET.get('firstname')
    lastname = request.GET.get('lastname')
    birth = request.GET.get('birth')
    e_mail = request.GET.get('e_mail')
    phone = request.GET.get('phone')
    sotial_vk = request.GET.get('sotial_vk')
    sotial_ok = request.GET.get('sotial_ok')
    sotial_inst = request.GET.get('sotial_inst')
    sotial_tube = request.GET.get('sotial_tube')

    about = request.GET.get('about')
    context = {
        'foto_html': photo_url,
        'photo_img': photo_img,
        'photo_ext': photo_ext,
        'firstname': firstname,
        'lastname': lastname,
        'birth_html': birth,
        'phone': phone,
        'e_mail': e_mail,
        'sotial_vk': sotial_vk,
        'sotial_ok': sotial_ok,
        'sotial_inst': sotial_inst,
        'sotial_tube': sotial_tube,
        'about': about,
        'page_name': verbose_name,
        'page_style': app_name
    }
    return render(request, template_name=f'./{app_name}/{app_name}.html',context=context)
