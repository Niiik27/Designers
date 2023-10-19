from django.shortcuts import render, get_object_or_404, redirect
from APP_NAMES import APP_NAMES, VERBOSE_APP_NAMES
from loginuser.models import UserProfile
app_name = APP_NAMES.HOME
verbose_name = VERBOSE_APP_NAMES.HOME
def homeView(request):
    print(dir(request.user))
    print(request.user.username)

    if request.user.username:
        return redirect("/" + request.user.username)
    else:
        return redirect(f"/{APP_NAMES.ARTISTS}")
        # return render(request, template_name=f'./{app_name}/{app_name}.html', context={'page_name':verbose_name,'page_style':app_name})

