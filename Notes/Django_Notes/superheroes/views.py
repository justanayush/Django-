from django.shortcuts import render
from .models import DC_Sups
from django.shortcuts import get_object_or_404

# Create your views here.
def dc_sup(request):
    sups = DC_Sups.objects.all
    return render(request,'superheroes/all_sup.html', {'sups': sups})

def sup_detail(request, sup_id):
    sup = get_object_or_404(DC_Sups, pk=sup_id)
    return render(request , 'superheroes/sup_detail.html',{'sup': sup})