from django import forms
 
class freelanceFormulario(forms.Form):
    id= forms.IntegerField()
    nombre = forms.CharField()
    mail = forms.EmailField()
    profesión = forms.CharField()
    servicios = forms.CharField()

class contratadorFormulario(forms.Form):
    id= forms.IntegerField()
    nombre = forms.CharField()
    mail = forms.EmailField()
    profesión = forms.CharField()
    servicios = forms.CharField()