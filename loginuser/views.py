from pprint import pprint

from APP_NAMES import APP_NAMES, VERBOSE_APP_NAMES

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User  # подключение Базы данных по умолчанию
from django.contrib.auth import login, authenticate, logout
from django.db import IntegrityError
from .forms import UserProfileForm
from .models import UserProfile
from django.contrib.auth.decorators import login_required
from django.contrib import messages

app_name = APP_NAMES.LOGIN_USER
verbose_name = VERBOSE_APP_NAMES.LOGIN_USER


def reguserView(request):
    if request.method == "GET":
        return render(request, f'{APP_NAMES.REG_USER}/{APP_NAMES.REG_USER}.html',
                      {'page_name': VERBOSE_APP_NAMES.REG_USER, 'page_style': APP_NAMES.REG_USER})
    else:
        print(
            "wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww")
        if request.POST['password1'] == request.POST['password2']:
            try:
                print(
                    "wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww")
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                print(
                    "wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww")
                print(User)
                user.save()
                print(UserProfile.__dict__)
                print(type(request.POST))
                print(request.POST)
                #photo_url = photo_url, image = image, firstname = firstname, lastname = lastname, birth = birth, e_mail = e_mail, phone = phone, sotial_vk = sotial_vk, sotial_ok = sotial_ok, sotial_inst = sotial_inst, sotial_tube = sotial_tube, username = username, password = password, about = about, user = user
                userProfile = UserProfile.create_user_profile(request.POST)

                print(
                    "wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww")

                login(request, user)
                return redirect('home')
            except IntegrityError:
                return render(request, 'reguser/reguser.html',
                              {'formuser': UserCreationForm(), 'error': 'Такой логин уже занят',
                               'page_name': 'Регистрация - выберите другой логин'})
        else:
            return render(request, 'reguser/reguser.html',
                          {'formuser': UserCreationForm(), 'error': 'Пароли не совпадают',
                           'page_name': 'Введите совпадающие пароли', })


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
                          {'formuser': form, 'error': 'Неверный логин или пароль1', 'page_name': 'Вход'})
        except AttributeError:  # Альтернатива else
            return render(request, f'{app_name}/login.html',
                          {'formuser': form, 'error': 'Неверный логин или пароль2', 'page_name': 'Вход'})
    else:
        return render(request, f'{app_name}/login.html',
                      {'formuser': form, 'error': 'Неверный логин или пароль3', 'page_name': 'Вход'})


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
