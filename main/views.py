from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'index.html')

def ads(request, ad_id):
    return HttpResponse(f"<h1>Объявление №{ad_id}</h1>")