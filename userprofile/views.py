from django.shortcuts import render
app_name='userprofile'
def profileView(request):
    return render(request, template_name=f'./{app_name}/{app_name}.html', context={'page_name':'Профиль проектанта','page_style':app_name})
