from django.shortcuts import render
# from .models import Article
app_name = 'blog'
def blogView(request):
    return render(request, template_name=f'./{app_name}/{app_name}.html', context={'page_name':'Блог','page_style':app_name})
sub_app_name = 'blog'
def detailView(request, article_id):
    # article = get_object_or_404(Article, pk = article_id)
    return render(request, template_name=f'./{sub_app_name}/{sub_app_name}.html',
                  context={'page_name': 'Статья', 'page_style': sub_app_name})