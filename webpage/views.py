from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

def indexPage(request):
    return render(request, "index.html")

def aboutPage(request):
    return render(request, "about.html")

def contactPage(request):
    return render(request, 'contact.html')
