from django.shortcuts import render, get_object_or_404
from Bill.models import Facture
# Create your views here.

def DetailFactureView(request, pk):
    facture = get_object_or_404(Facture, id=pk)
    context={}
    context['facture'] = facture
    return render(request, 'bill/facture_detail.html', context)