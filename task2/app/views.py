from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def main(request):
    return HttpResponse("""
    <form method="GET" action="/greet/">
    <input type="text" name="name" placeholder="Enter your name">
    <button type="submit">Submit</button>
</form>
<form method="GET" action="/greet_full/">
    <input type="text" name="name" placeholder="Enter your name">
    <input type="text" name="surname" placeholder="Enter your surname">
    <button type="submit">Submit</button>
</form>
    <form method='POST' action='/create/'>
                            <input type='text' name='name'>
                            <input type='text' name='surname'>
                            <button type='submit'>Submit</button>
                         </form>""")

def greet(request):
    name = request.GET.get('name', '')
    return HttpResponse(f'Hello, {name}!')

def greet_full(request):
    name = request.GET.get('name', '')
    surname = request.GET.get('surname', '')
    return HttpResponse(f'Hello, {name} {surname}!')


@csrf_exempt
def create(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        surname = request.POST.get('surname', '')

        return HttpResponse(f'User {name} {surname} created successfully!')
    return HttpResponse('Invalid request method.')