from django import forms

class DateDeTraitement(forms.Form):
    """
    docstring
    """
    date_traitement = forms.DateField(label='Date de Traitement')