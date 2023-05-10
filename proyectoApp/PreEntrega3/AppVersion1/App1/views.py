from django.shortcuts import render
#from django.template import loader 
from .models import Acceso, Servicios, Freelance, Contratador
from .forms import freelanceFormulario, contratadorFormulario
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm 
from django.contrib.auth import login,logout,authenticate
from App1.forms import UserRegisterForm

# Create your views here.
def inicio(request):
    return render (request,"App1/inicio.html")
def Acceso(request):
    return render (request,"App1/Acceso.html")
def Freelance(request):
    return render (request,"App1/Freelance.html")
def Contratador(request):
    return render (request,"App1/Contratador.html")
def Servicios(request):
    return render (request,"App1/Servicios.html")

def freelance_view(request):
      if request.method == "POST":
            miFormulario = freelanceFormulario(request.POST) # Aqui me llega la informacion del html
            print(miFormulario)

            if miFormulario.is_valid:
                  informacion = miFormulario.cleaned_data
                  Freelance =  Freelance(int(informacion['id']),str(informacion['nombre']),str(informacion['mail']),str(informacion['profesion']),str(informacion['servicios']))
                  Freelance.save()
                  return render(request, "App1/inicio.html")
      else:
            miFormulario = freelanceFormulario()
 
      return render(request, "App1/Freelance.html", {"miFormulario": miFormulario})


def contratador_view (request):
     if request.method == "POST":
        miFormulario = contratadorFormulario(request.POST) 
        print(miFormulario)
        
        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            Contratador = Contratador(int(informacion['id']),str(informacion['nombre']),str(informacion['mail']),str(informacion['profesion']),str(informacion['servicios']))
            Contratador.save()
            return render(request, "App1/inicio.html")
     else:
        miFormulario = contratadorFormulario()
             
     return render(request, "App1/Contratador.html", {"miFormulario": miFormulario})

def busquedaFreelance(request):
     return render(request,'App1/busquedaFreelance.html')

def buscar(request):
     if request.GET['Freelance']:
          Freelance = request.GET['Freelance']
          Freelance = Freelance.objects.filter(Freelance__icontains=Freelance)

          return render(request,'App1/inicio.html', {"nombre":Freelance, "mail": Freelance })
     else:
          respuesta= "No enviaste datos"

     return HttpResponse(respuesta)


def leerFreelance(request):
    Freelances= Freelance.objects.all()     
    contexto= {"Freelance": Freelances}
    return render(request, "App1/leerFreelance.html",contexto)

def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():  # Si pasó la validación de Django
            usuario = form.cleaned_data.get('username')
            contrasenia = form.cleaned_data.get('password')
            user = authenticate(username= usuario, password=contrasenia)
            if user is not None:
                login(request, user)
                return render(request, "App1/inicio.html", {"mensaje":f"Bienvenido {usuario}"})
            else:
                return render(request, "App1/inicio.html", {"mensaje":"Datos incorrectos"})
        else:
            return render(request, "App1/inicio.html", {"mensaje":"Formulario erroneo"})
    form = AuthenticationForm()
    return render(request, "App1/login.html", {"form": form})


def register(request):
      if request.method == 'POST':
            #form = UserCreationForm(request.POST)
            form = UserRegisterForm(request.POST)
            if form.is_valid():
                  username = form.cleaned_data['username']
                  form.save()
                  return render(request,"App1/inicio.html" ,  {"mensaje":"Usuario Creado :)"})
      else:
            #form = UserCreationForm()       
            form = UserRegisterForm()     
      return render(request,"App1/registro.html" ,  {"form":form})


