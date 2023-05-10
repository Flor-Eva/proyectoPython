from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
 
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

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        # Saca los mensajes de ayuda
        help_texts = {k:"" for k in fields}