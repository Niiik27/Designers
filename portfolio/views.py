from django.db import OperationalError
from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404
from APP_NAMES import APP_NAMES, VERBOSE_APP_NAMES
from loginuser.models import UserProfile
from .forms import ArtworkForm

# from django.db import models
app_name = APP_NAMES.PORTFOLIO
from .models import Artwork

verbose_name = VERBOSE_APP_NAMES.PORTFOLIO


def portfolioView(request):
    print(request)
    print(type(request))
    print(dir(request))
    print(request.user.id)
    print(dir(request.user))  # Откуда же здесь берется юзер?
    print(request.method)
    if request.method == 'GET':
        print('****portfolio****', 'portfolio')
        print('****portfolio****', request.user.username)
        try:
            portfolio = Artwork.objects.all()
            # portfolio = get_object_or_404(Artwork, username=request.user.username)
            # print(dir(portfolio.image))
            # print(portfolio.image.path)
        except Http404 as e:
            print(str(e))
            portfolio = None
            # print('****portfolio****',portfolio)
            # print(dir(portfolio.image))
        except OperationalError as e:
            print(str(e))
            portfolio = None
        form = ArtworkForm()
        return render(request, template_name=f'./{app_name}/{app_name}.html',
                      context={'form': form, 'portfolio': portfolio, 'page_name': verbose_name, 'page_style': app_name})

    else:
        # print('****portfolio****', 'portfolio')
        # print('****portfolio****', 'portfolio')
        # print('****portfolio****', 'portfolio')
        # print('****portfolio****', 'portfolio')
        # print('****portfolio****', 'portfolio')
        # print((dict(request.FILES)).keys())
        # print(request.POST)
        # instance = request.user.userprofile
        # print(instance)

        form = ArtworkForm(request.POST, request.FILES)
        if form.is_valid():
            artwork = form.save(commit=False)
            artwork.user = request.user
            artwork.save()
        # artwork = Artwork(
        # user = request.user,
        # title = request.POST['title'],
        # desc = request.POST['desc'],
        # image = request.FILES,
        # date = request.POST['img_data'],
        # url = request.POST['partners'],
        # )
        # artwork.save()
        # print(artwork.image.upload_to)
        # return redirect("/" + request.user.username)
        return redirect(APP_NAMES.PORTFOLIO)
