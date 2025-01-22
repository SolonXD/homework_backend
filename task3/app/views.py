from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from .models import Model

# Create your views here.

def main(request):
    return HttpResponse(f"""<form method='POST' action='/greet_or_redirect/'>
                                <input type='text' name='make_user'>
                                <button type='submit'>Input name</button>
                            </form>
                            <form method='GET' action='/greet_or_redirect/'>
                                <input type='text' name='name'>
                                <button type='submit'>Get greeting</button>
                            </form>""")

@csrf_exempt
def greet_or_redirect(request):
    if request.method == 'POST':
        name = request.POST.get("make_user")
        Model.objects.create(name=name)
        return HttpResponseRedirect("/")

    elif request.method == 'GET':
        try:
            name = request.GET.get('name')
            name_ver = Model.objects.get(name=name)
            return HttpResponse(f'Hello, {name_ver}!')
        except Model.DoesNotExist:
            return HttpResponse(f'Hello, Guest!')


