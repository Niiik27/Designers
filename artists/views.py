from django.shortcuts import render
app_name = 'artists'
def artistsView(request, article_id):
    return render(request, template_name=f'./{app_name}/{app_name}.html',
                  context={'page_name': 'Проектанты', 'page_style': app_name})