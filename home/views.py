from django.shortcuts import render
app_name = 'home'
def homeView(request):
    return render(request, template_name=f'./{app_name}/{app_name}.html', context={'page_name':'Стартовая страница','page_style':app_name})
