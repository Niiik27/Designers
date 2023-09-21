from django.shortcuts import render
app_name='usermessages'
def messageView(request):
    return render(request, template_name=f'./{app_name}/{app_name}.html', context={'page_name':'Сообщения','page_style':app_name})
