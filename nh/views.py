from django.shortcuts import render

def menu(request):
    """
    docstring
    """
    return render(request, 'pages/menu.html')

def sls(request):
    """
    docstring
    """
    return render(request, 'pages/sls.html')

def quittance(request):
    """
    docstring
    """
    return render(request, 'pages/quittance.html')

def regularisation(request):
    """
    docstring
    """
    return render(request, 'pages/regularisation.html')

def relance(request):
    """
    docstring
    """
    return render(request, 'pages/relance.html')