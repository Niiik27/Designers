from django.shortcuts import render, redirect, get_object_or_404
from APP_NAMES import APP_NAMES, VERBOSE_APP_NAMES
from loginuser.models import UserProfile

# from django.db import models
app_name = APP_NAMES.PORTFOLIO
from .models import Artwork
verbose_name = VERBOSE_APP_NAMES.PORTFOLIO

def portfolioView(request):
    print(request)
    print(type(request))
    print(dir(request))
    print(request.user.id)
    print(dir(request.user))# Откуда же здесь берется юзер?
    print(request.method)
    if request.method == 'GET':
        portfolio = get_object_or_404(Artwork, username=request.user.username)
        return render(request, template_name=f'./{app_name}/{app_name}.html', context={'portfolio':portfolio,'page_name':verbose_name,'page_style':app_name})
    else:

        artwork = Artwork(
        username = request.user.username,
        title = request.POST['title'],
        desc = request.POST['desc'],
        image = request.POST['artwork'],
        date = request.POST['img_data'],
        url = request.POST['partners'],
        )
        artwork.save()
        # return redirect("/" + request.user.username)
        return redirect(APP_NAMES.PORTFOLIO)