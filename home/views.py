from django.shortcuts import render, get_object_or_404
from APP_NAMES import APP_NAMES, VERBOSE_APP_NAMES
from loginuser.models import UserProfile
app_name = APP_NAMES.HOME
verbose_name = VERBOSE_APP_NAMES.HOME
def homeView(request):
    return render(request, template_name=f'./{app_name}/{app_name}.html', context={'page_name':verbose_name,'page_style':app_name})

def profileView(request, username):
    user = get_object_or_404(UserProfile, username = username)
    return render(request, f'./{app_name}/{app_name}.html',{'user':user, 'page_name':'Статья','page_style':'detail'})
