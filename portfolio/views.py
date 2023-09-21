from django.shortcuts import render
app_name='portfolio'
def portfolioView(request):
    return render(request, template_name=f'./{app_name}/{app_name}.html', context={'page_name':'Портфолио','page_style':app_name})
