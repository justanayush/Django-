from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("Hello World")
    return render(request, 'website/index.html')


def about(request):
    return HttpResponse("Hello World about")

def contact(request):
    return HttpResponse("Hello World contact")



