from django.shortcuts import render, redirect
from APP_NAMES import APP_NAMES, VERBOSE_APP_NAMES
from loginuser.models import UserProfile
from django.db.models import Q

app_name = APP_NAMES.PARTNERS
verbose_name = VERBOSE_APP_NAMES.PARTNERS
def partnersView(request):
    return render(request, template_name=f'./{app_name}/{app_name}.html', context={'page_name':verbose_name,'page_style':app_name})

def partnersView(request):
    # users = UserProfile.objects.all()

    # UserProfile.objects.all().filter(Q(purpose='sailor') | Q(purpose='3d_maker'))

    users = UserProfile.objects.all().filter(Q(purpose='sailor') | Q(purpose='3d_maker'))
    if users:
        return render(request, f'{app_name}/{app_name}.html',{'users':users, 'page_name':verbose_name,'page_style':verbose_name})
    else:
        return redirect(request,APP_NAMES.HOME)