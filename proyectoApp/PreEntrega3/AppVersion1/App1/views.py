from django.shortcuts import render
#from django.template import loader 
from .models import Acceso, Servicios, Freelance, Contratador
from .forms import freelanceFormulario, contratadorFormulario
from django.http import HttpResponse

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

def Freelance(request):
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


def Contratado (request):
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
             
     return render(request, "App1/Contratador.html.html", {"miFormulario": miFormulario})

def busquedaFreelance(request):
     return render(request,'App1/busquedaFreelance.html')

def buscar(request):
     if request.GET['Freelance']:
          Freelance = request.GET['Freelance']
          Freelance = Freelance.objects.filter(Freelance__icontains=Freelance)

          return render(request,'App1/resultadosBusqueda.html', {"nombre":Freelance, "mail": Freelance })
     else:
          respuesta= "No enviaste datos"

     return HttpResponse(respuesta)



