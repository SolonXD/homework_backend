from django.shortcuts import render
from django.http import JsonResponse

def process_request(request):
    return JsonResponse({"message": "Status: 200"})
