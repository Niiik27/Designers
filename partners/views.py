from django.shortcuts import render
app_name = 'partners'
def partnersView(request):
    return render(request, template_name=f'./{app_name}/{app_name}.html', context={'page_name':'Партнеры','page_style':app_name})

