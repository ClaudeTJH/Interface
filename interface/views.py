from django.shortcuts import render

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
    return render(request, 'home/p2r.html')