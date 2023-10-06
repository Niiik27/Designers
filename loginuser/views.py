from pprint import pprint
from io import BytesIO
import requests
from PIL import Image
from APP_NAMES import APP_NAMES, VERBOSE_APP_NAMES

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User  # подключение Базы данных по умолчанию
from django.contrib.auth import login, authenticate, logout
from django.db import IntegrityError
from .forms import UserProfileForm
from .models import UserProfile
from django.contrib.auth.decorators import login_required
from django.core.files.base import ContentFile
from django.contrib import messages

app_name = APP_NAMES.LOGIN_USER
verbose_name = VERBOSE_APP_NAMES.LOGIN_USER


def save_image_from_url(url):
    response = requests.get(url)
    if response.status_code == 200:
        img_data = BytesIO(response.content)
        img = Image.open(img_data)

        new_size = (300, 300)
        img.thumbnail(new_size)

        pathURL = url.split("?")[0]
        imgExt = pathURL[pathURL.rfind('.') + 1:len(pathURL)]
        if imgExt.lower() == 'jpg':
            imgExt = 'jpeg'
        filename = pathURL.split('/')[-1]

        # Преобразуем изображение в байты
        buffer = BytesIO()
        img.save(buffer, format=imgExt)
        image_file = ContentFile(buffer.getvalue())

        # Сохраняем изображение в поле ImageField
        # self.image.save(filename, image_file)
        return image_file

def reguserView(request):
    if request.method == "GET":
        return render(request, f'{APP_NAMES.REG_USER}/{APP_NAMES.REG_USER}.html',
                      {'page_name': VERBOSE_APP_NAMES.REG_USER, 'page_style': APP_NAMES.REG_USER})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                # userProfile = UserProfile.create_user_profile(request.POST)

                userProfile = UserProfile(
                photo_url = request.POST['photo_url'],
                image = save_image_from_url(request.POST['photo_url']),
                firstname = request.POST['firstname'],
                lastname = request.POST['lastname'],
                birth = request.POST['birth'],
                e_mail = request.POST['e_mail'],
                phone = request.POST['phone'],
                social_vk = request.POST['social_vk'],
                social_ok = request.POST['social_ok'],
                social_inst = request.POST['social_inst'],
                social_tube = request.POST['social_tube'],
                username = request.POST['username'],
                password = request.POST['password1'],
                about = request.POST['about'],
                )



                print("3" * 150)
                userProfile.save()
                print("4"*150)

                login(request, user)
                print("5" * 255)
                return redirect('home')
            except IntegrityError as e:
                error_message = str(e)
                print(f'Произошла ошибка: {error_message}')
                return render(request, 'reguser/reguser.html',
                              {'formuser': UserCreationForm(), 'error': 'Такой логин уже занят',
                               'page_name': 'Регистрация - выберите другой логин', 'page_style': app_name})
        else:
            return render(request, 'reguser/reguser.html',
                          {'formuser': UserCreationForm(), 'error': 'Пароли не совпадают',
                           'page_name': 'Введите совпадающие пароли', 'page_style': app_name, })


def loginuserView(request):
    if request.method == 'GET':
        return render(request, f'{app_name}/{app_name}.html', {'page_name': verbose_name, 'page_style': app_name})
    else:
        form = AuthenticationForm(request.POST)
        user = authenticate(username=request.POST['username'], password=request.POST['password'])

    if user is not None:
        try:
            login(request, user)
            return redirect('home')
        except ValueError:
            return render(request, f'{app_name}/login.html',
                          {'formuser': form, 'error': 'Неверный логин или пароль1', 'page_name': 'Вход', 'page_style': app_name})
        except AttributeError:  # Альтернатива else
            return render(request, f'{app_name}/login.html',
                          {'formuser': form, 'error': 'Неверный логин или пароль2', 'page_name': 'Вход', 'page_style': app_name})
    else:
        return render(request, f'{app_name}/login.html',
                      {'formuser': form, 'error': 'Неверный логин или пароль3', 'page_name': 'Вход', 'page_style': app_name})


def logoutuserView(request):
    logout(request)
    return redirect('home')


def profileView(request):
    user_profile = request.user
    return render(request, f'{APP_NAMES.USER_PROFILE}/{APP_NAMES.USER_PROFILE}.html', {user_profile: 'user_profile'})


def profileupView(request):
    user_profile = request.user.userprofile
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=user_profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Профиль успешно обновлен')
            return redirect('profile')
    else:
        form = UserProfileForm(instance=user_profile)
        return render(request, 'profile/profileup.html', {'form': form})
