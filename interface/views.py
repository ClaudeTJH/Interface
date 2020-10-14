from django.shortcuts import render

from .fonctions import lance_application

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