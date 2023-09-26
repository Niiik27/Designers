from django.shortcuts import render
from APP_NAMES import APP_NAMES, VERBOSE_APP_NAMES

app_name = APP_NAMES.PORTFOLIO
verbose_name = VERBOSE_APP_NAMES.PORTFOLIO

def portfolioView(request):
    return render(request, template_name=f'./{app_name}/{app_name}.html', context={'page_name':verbose_name,'page_style':app_name})
