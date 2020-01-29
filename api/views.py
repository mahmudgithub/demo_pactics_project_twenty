from django.shortcuts import render

# Create your views here.
from django.http.response import JsonResponse


def lol(request):
    return JsonResponse({"message": "hello world!"})