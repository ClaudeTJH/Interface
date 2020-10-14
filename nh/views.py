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

# def LorenzMieView(request):
#     if request.method == 'POST':
#         form = LorenzMieForm(request.POST)
#         if form.is_valid():
#             Submitted_Wavelength = form.cleaned_data[ 'Wavelength' ]
#             Submitted_SphereRadius = form.cleaned_data[ 'SphereRadius' ]
#             Submitted_RealPart = form.cleaned_data[ 'RealPart' ]
#             Submitted_ImaginaryPart = form.cleaned_data[ 'ImaginaryPart' ]
#             print (Submitted_Wavelength, Submitted_SphereRadius, \
#             Submitted_RealPart, Submitted_ImaginaryPart)
#             # Do something
#     else:
#         form = LorenzMieForm()
#     return render(request, "pages/test.html", 
#     {'form':form})