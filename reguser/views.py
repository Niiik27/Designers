from django.shortcuts import render
app_name='reguser'
def reguserView(request):
    return render(request, template_name=f'./{app_name}/{app_name}.html', context={'page_name':'Регистрация','page_style':app_name})
