from io import BytesIO

from PIL import Image
from django.core.files.base import ContentFile
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.db import OperationalError
from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404
from APP_NAMES import APP_NAMES, VERBOSE_APP_NAMES
from loginuser.models import UserProfile
from .forms import ArtworkForm

app_name = APP_NAMES.PORTFOLIO
from .models import Artwork

verbose_name = VERBOSE_APP_NAMES.PORTFOLIO



def get_date(date):
    day_list = ['первое', 'второе', 'третье', 'четвёртое',
                'пятое', 'шестое', 'седьмое', 'восьмое',
                'девятое', 'десятое', 'одиннадцатое', 'двенадцатое',
                'тринадцатое', 'четырнадцатое', 'пятнадцатое', 'шестнадцатое',
                'семнадцатое', 'восемнадцатое', 'девятнадцатое', 'двадцатое',
                'двадцать первое', 'двадцать второе', 'двадцать третье',
                'двадацать четвёртое', 'двадцать пятое', 'двадцать шестое',
                'двадцать седьмое', 'двадцать восьмое', 'двадцать девятое',
                'тридцатое', 'тридцать первое']
    month_list = ['января', 'февраля', 'марта', 'апреля', 'мая', 'июня',
                  'июля', 'августа', 'сентября', 'октября', 'ноября', 'декабря']

    newdate = date[:date.rindex(' ')]
    year = int(newdate[newdate.rindex(' '):len(newdate)])
    newdate = date[:newdate.rindex(' ')]
    month_str = str(newdate[newdate.rindex(' '):len(newdate)]).strip(' ')
    day_str = date[:newdate.rindex(' ')].strip(' ')

    day = str(day_list.index(day_str)+1).rjust(2,'0')
    month = str(month_list.index(month_str)+1).rjust(2, '0')

    return f'{year}-{month}-{day}'


def make_thumb(image:InMemoryUploadedFile):
    imgIO = image.read()
    img_data = BytesIO(imgIO)
    img = Image.open(img_data)



    new_size = (300, 300)
    img.thumbnail(new_size)

    filenames = image.name
    imgnames = filenames.split('.')
    imgExt = imgnames[1]
    filename = imgnames[0]
    print(filename)

    # Преобразуем изображение в байты
    buffer = BytesIO()
    img.save(buffer, format=imgExt)
    image_file = ContentFile(buffer.getvalue(),name=filename)
    InMemoryUploadedFile(file=image_file,name=filename, content_type='image/jpeg')

    return image_file

def portfolioView(request):
    # print(request)
    # print(type(request))
    # print(dir(request))
    # print(request.user.id)
    # print(dir(request.user))  # Откуда же здесь берется юзер?
    print(request.method)
    print("2" * 200)
    if request.method == 'GET':
        # print('****portfolio****', 'portfolio')
        # print('****portfolio****', request.user.username)
        try:
            portfolio = Artwork.objects.filter(user=request.user)

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

        edit_mode = request.POST['edit_mode']
        match edit_mode:
            case 'new_image':
                print('FILESFILESFILES',request.FILES)
                make_thumb(request.FILES['image'])
                form = ArtworkForm(request.POST, request.FILES)
                if form.is_valid():
                    artwork = form.save(commit=False)
                    artwork.user = request.user
                    artwork.save()

                    portfolio = Artwork.objects.filter(user=request.user, id=artwork.id)
                    portfolio.update(thumb=make_thumb(request.FILES['image']))
                return redirect(APP_NAMES.PORTFOLIO)
            case 'edit_image':
                print('changed')
                print(request.POST['id'])
                img_id = request.POST['id']
                portfolio = Artwork.objects.filter(user=request.user, id=img_id)
                print(portfolio)

                edit_img = request.POST['image']
                edit_title = request.POST['title']
                edit_desc = request.POST['desc']
                edit_date = request.POST['date']
                edit_url = request.POST['url']
                if edit_img:
                    portfolio.update(image=edit_img)
                if edit_title:
                    portfolio.update(title=edit_title)
                portfolio.update(desc=edit_desc)
                portfolio.update(date=get_date(edit_date))
                portfolio.update(url=edit_url)
                # portfolio.update(id = edit_url)

                return redirect(APP_NAMES.PORTFOLIO)
            case 'delete_image':
                print('deleted')
                img_id = request.POST['id']
                portfolio = Artwork.objects.filter(user=request.user, id=img_id)
                portfolio.delete()
                return redirect(APP_NAMES.PORTFOLIO)
            case _:
                print('error')
                return redirect(APP_NAMES.PORTFOLIO)
