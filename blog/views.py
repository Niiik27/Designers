from django.shortcuts import render
# from .models import Article
from APP_NAMES import APP_NAMES, VERBOSE_APP_NAMES

app_name = APP_NAMES.BLOG
verbose_name = VERBOSE_APP_NAMES.BLOG
def blogView(request):
    return render(request, template_name=f'./{app_name}/{app_name}.html', context={'page_name':verbose_name,'page_style':app_name})
sub_app_name = 'blog'
def detailView(request, article_id):
    # article = get_object_or_404(Article, pk = article_id)
    return render(request, template_name=f'./{sub_app_name}/{sub_app_name}.html',
                  context={'page_name': 'Статья', 'page_style': sub_app_name})