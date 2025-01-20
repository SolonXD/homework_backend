from django.shortcuts import render, HttpResponse


# Create your views here.

def about(request):
    return HttpResponse("<h1>Second Page</h1>")


def main(request):
    return HttpResponse("<h1>Main</h1>")
