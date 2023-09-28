from django.shortcuts import render, get_object_or_404
from APP_NAMES import APP_NAMES, VERBOSE_APP_NAMES
from .models import MyEvent
app_name = APP_NAMES.EVENTS
verbose_app_name = VERBOSE_APP_NAMES.EVENTS

def eventsView(request):
    # events = MyEvent
    return render(request, template_name=f'./{app_name}/{app_name}.html', context={'events':'events','page_name':verbose_app_name, 'page_style':app_name})

# def detailView(request, event_id):
#     event = get_object_or_404(MyEvent, pk = event_id)
#     return render(request, 'detail/detail.html',{'event':event, 'page_name':event.title,'page_style':app_name})