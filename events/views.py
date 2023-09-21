from django.shortcuts import render
app_name = 'events'

def eventsView(request):
    return render(request, template_name=f'./{app_name}/{app_name}.html', context={'page_name':'События','page_style':app_name})
