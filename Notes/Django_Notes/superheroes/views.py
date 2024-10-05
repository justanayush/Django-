from django.shortcuts import render

# Create your views here.
def dc_sup(request):
    return render(request,'superheroes/all_sup.html')