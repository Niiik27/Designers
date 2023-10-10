from django.shortcuts import render, get_object_or_404
from .models import Article
from APP_NAMES import APP_NAMES, VERBOSE_APP_NAMES

app_name = APP_NAMES.BLOG
verbose_name = VERBOSE_APP_NAMES.BLOG
def blogView(request):
    articles = Article.objects.all()
    return render(request, template_name=f'./{app_name}/{app_name}.html', context={'articles': articles, 'page_name':verbose_name,'page_style':app_name})

def detailView(request, article_id):
    article = get_object_or_404(Article, pk = article_id)
    return render(request, template_name=f'./{APP_NAMES.ARTICLE}/{APP_NAMES.ARTICLE}.html',
                  context={APP_NAMES.ARTICLE:article, 'page_name': VERBOSE_APP_NAMES.ARTICLE, 'page_style': APP_NAMES.ARTICLE})