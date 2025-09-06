# from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    # return HttpResponse("Hello, django!")
    return render(request, 'home.html')