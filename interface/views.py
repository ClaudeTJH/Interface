import os

from django.shortcuts import render

from .fonctions import lance_application
from .forms import DateDeTraitement

def index(request):
    """
    docstring
    """
    return render(request, 'home/index.html')

def enveloppe(request):
    """
    docstring
    """
    return render(request, 'home/enveloppe.html')

def lindab(request):
    """
    docstring
    """
    if request.method == 'POST':
        form = DateDeTraitement(request.POST)
        if form.is_valid():
            return render(request, 'home/lindab.html', {'form': form.as_p})
        # return render(request, 'layouts/prise_en_compte.html')
    return render(request, 'home/lindab.html')

def mif(request):
    """
    docstring
    """
    return render(request, 'home/mif.html')

def p2r(request):
    """
    docstring
    """
    if request.method == 'POST':
        lance_application(lanceur='p2r')
        return render(request, 'layouts/prise_en_compte.html')
    return render(request, 'home/p2r.html')