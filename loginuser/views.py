from datetime import date
from pprint import pprint
from io import BytesIO
import re

import requests
from PIL import Image
from django.http import Http404

from APP_NAMES import APP_NAMES, VERBOSE_APP_NAMES
from django.db import models
from django.shortcuts import render, redirect, get_object_or_404
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
        image_file = ContentFile(buffer.getvalue(),name=filename)

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
                try:
                    user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                    user.save()
                    print("Новый вход")
                    print("создадся пользователь")
                except IntegrityError:
                    print("Не получилось создать пользователя потому что такой уже существует")
                    if request.user.is_authenticated:
                        user = request.user
                        print('Вход под залогининым пользователем')
                        print('Такое возможно если залогинились неимея инфо')
                        print('Такое возможно если входили в админку под суперпользователем, которого создали в django, но не через страницу регистрации')
                        print('И такое возможно при редактировании пользователя')
                    else:
                        user = get_object_or_404(User, username=request.POST['username'])
                        print('Такой пользователь уже есть и он взят из базы')
                        print('Такое возможно при входе. Возможно это старый вариант для суперпользователя. требуется отследить')
                        print('')
                try:
                    print(f'Пошло по 1 пути, в любом случае мы получили пользователя, теперь нам нужно получить его инфо')
                    userProfile = get_object_or_404(UserProfile, username=user.username)
                    print(f'Профиль пользователя найден')
                    print('Это значит что происходит редактирование инфо')
                    print('Значит сюда попали со страницы редактирования')
                    userProfile.photo_url = request.POST['photo_url']
                    userProfile.image = save_image_from_url(request.POST['photo_url'])
                    userProfile.firstname = request.POST['firstname']
                    userProfile.lastname = request.POST['lastname']
                    userProfile.birth = request.POST['birth']
                    userProfile.e_mail = request.POST['e_mail']
                    userProfile.phone = ''.join(re.findall("\d+", request.POST['phone']))
                    userProfile.purpose = request.POST.get('purpose')
                    userProfile.social_vk = request.POST['social_vk']
                    userProfile.social_ok = request.POST['social_ok']
                    userProfile.social_inst = request.POST['social_inst']
                    userProfile.social_tube = request.POST['social_tube']
                    userProfile.username = request.POST['username'],
                    userProfile.password = request.POST['password1']
                    userProfile.about = request.POST['about']
                    # print(request.user)
                    # print(request.user.username)
                    # print(request.user)
                    userProfile.user = user
                    print(f'Все ок прошло по 1 пути')

                except Http404:
                    print("Профиль не нашелся,  создается новый")
                    print("Это произошло потому что нет инфо")


                    if request.user.is_authenticated:
                        print("Произошел вход СУПЕРПОЛЬЗОВАТЕЛЯ, создается для него инфо")
                    else:
                        print("Создается инфо для нового пользователя")

                    userProfile = UserProfile(
                    photo_url = request.POST['photo_url'],
                    image = save_image_from_url(request.POST['photo_url']),
                    firstname = request.POST['firstname'],
                    lastname = request.POST['lastname'],
                    birth = request.POST['birth'],
                    e_mail = request.POST['e_mail'],
                    phone = ''.join(re.findall("\d+", request.POST['phone'])),
                    purpose = request.POST.get('purpose'),
                    social_vk = request.POST['social_vk'],
                    social_ok = request.POST['social_ok'],
                    social_inst = request.POST['social_inst'],
                    social_tube = request.POST['social_tube'],
                    username = request.POST['username'],
                    password = request.POST['password1'],
                    about = request.POST['about'],
                    user = user,
                    )
                print("Новый профиль создался")
                userProfile.save()
                print("Новый профиль сохранился")
                login(request, user)
                print("Новый профиль заллогинился")
                return redirect("/"+user.username)


            except IntegrityError as e:
                if request.user.is_authenticated:
                    print("Пошло по 2 пути")
                    print(e)
                    # userProfile = get_object_or_404(UserProfile, username=user.username)
                    #
                    # userProfile.photo_url = request.POST['photo_url']
                    # userProfile.image = save_image_from_url(request.POST['photo_url'])
                    # userProfile.firstname = request.POST['firstname']
                    # userProfile.lastname = request.POST['lastname']
                    # userProfile.birth = request.POST['birth']
                    # userProfile.e_mail = request.POST['e_mail']
                    # userProfile.phone = ''.join(re.findall("\d+", request.POST['phone']))
                    # userProfile.purpose = request.POST.get('purpose')
                    # userProfile.social_vk = request.POST['social_vk']
                    # userProfile.social_ok = request.POST['social_ok']
                    # userProfile.social_inst = request.POST['social_inst']
                    # userProfile.social_tube = request.POST['social_tube']
                    # userProfile.username = request.POST['username'],
                    # userProfile.password = request.POST['password1']
                    # userProfile.about = request.POST['about']
                    # userProfile.user = user
                    # userProfile.save()
                    # login(request, user)
                    # print('Все ок на 2 пути')
                    # return redirect("/" + user.username)
                else:
                    error_message = str(e)
                    print(f'Произошла ошибка: {error_message}')
                    return render(request, f'{APP_NAMES.USER_PROFILE}/{APP_NAMES.USER_PROFILE}.html',
                                  {'error': 'Такой логин уже занят',
                                   'page_name': 'Регистрация - выберите другой логин', 'page_style': app_name})
        else:
            return render(request, f'{APP_NAMES.USER_PROFILE}/{APP_NAMES.USER_PROFILE}.html',
                      {'error': 'Пароли не совпадают',
                       'page_name': 'Введите совпадающие пароли', 'page_style': app_name, })


def loginuserView(request):
    if request.method == 'GET':
        return render(request, f'{app_name}/{app_name}.html', {'page_name': verbose_name, 'page_style': app_name})
    else:
        user = authenticate(username=request.POST['username'], password=request.POST['password'])

        if user is not None:
            try:
                login(request, user)
                return redirect("/"+user.username)
            except ValueError:
                return render(request, f'{app_name}/{app_name}.html',
                              {'error': 'Неверный логин или пароль1', 'page_name': 'Вход', 'page_style': app_name})
            except AttributeError:  # Альтернатива else
                return render(request, f'{app_name}/{app_name}.html',
                              {'error': 'Неверный логин или пароль2', 'page_name': 'Вход', 'page_style': app_name})
        else:
            return render(request, f'{app_name}/{app_name}.html',
                          {'error': 'Неверный логин или пароль3', 'page_name': 'Вход', 'page_style': app_name})


def logoutuserView(request):
    logout(request)
    return redirect('home')


def profileView(request, username):
    try:
        user = get_object_or_404(UserProfile, username = username)
        today = date.today()
        age = today.year - user.birth.year - ((today.month, today.day) < (user.birth.month, user.birth.day))
        # return render(request, f'{APP_NAMES.USER_PROFILE}/{APP_NAMES.USER_PROFILE}.html',{'user':user, 'page_name':VERBOSE_APP_NAMES.USER_PROFILE,'page_style':APP_NAMES.USER_PROFILE, 'age':age})
        return render(request, f'{APP_NAMES.HOME}/{APP_NAMES.HOME}.html',
                      {'userprofile': user, 'page_name': VERBOSE_APP_NAMES.HOME, 'page_style': APP_NAMES.HOME,
                       'age': age})

    except Http404:
        try:
            master_user = get_object_or_404(User, username = username)
            return redirect(f'/{APP_NAMES.LOGIN_USER}/{APP_NAMES.REG_USER}')
        except Http404:
            return redirect(f'/{APP_NAMES.ARTISTS}')



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
