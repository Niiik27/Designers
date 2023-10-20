from datetime import date

from django.shortcuts import render, redirect, get_object_or_404
from APP_NAMES import APP_NAMES, VERBOSE_APP_NAMES
from django.core.wsgi import get_wsgi_application

from django.contrib.auth.models import User  # подключение Базы данных по умолчанию
from django.contrib.auth import login, authenticate, logout
from django.db import IntegrityError
from loginuser.forms import UserProfileForm
from loginuser.models import UserProfile


app_name = APP_NAMES.ARTISTS
verbose_name = VERBOSE_APP_NAMES.ARTISTS
def artistsView(request):
    users = UserProfile.objects.all()
    users = UserProfile.objects.filter(purpose='diz')
    if users:
        return render(request, f'{app_name}/{app_name}.html',{'users':users, 'page_name':verbose_name,'page_style':verbose_name})
    else:
        return redirect(request,APP_NAMES.HOME)




def artis(request, username):
    user = get_object_or_404(UserProfile, username=username)
    today = date.today()
    age = today.year - user.birth.year - ((today.month, today.day) < (user.birth.month, user.birth.day))
    print(age)



    # return render(request, f'{APP_NAMES.USER_PROFILE}/{APP_NAMES.USER_PROFILE}.html',{'user':user, 'page_name':VERBOSE_APP_NAMES.USER_PROFILE,'page_style':APP_NAMES.USER_PROFILE, 'age':age})

    # return redirect(my_app)

    return render(request, f'artistcards/artist.html',
                  {'userprofile': user, 'page_name': VERBOSE_APP_NAMES.USER_PROFILE, 'page_style': APP_NAMES.USER_PROFILE, 'age': age})
