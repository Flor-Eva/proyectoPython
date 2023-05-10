from django.urls import path 
from App1 import views 

urlpatterns=[

    path('', views.inicio, name="Inicio"),
    path('Acceso', views.Acceso, name='Acceso'),
    path('Freelance', views.Freelance, name='Freelance'),
    path('Contratador', views.Contratador, name='Contratador'),
    path('Servicios', views.Servicios, name='Servicios'),
    path('contratadorFormulario', views.contratador_view, name='contratadorFormulario'),
    path('freelanceFormulario', views.freelance_view, name="freelanceFormulario"),
    path('busquedaFreelance', views.busquedaFreelance, name="busquedaFreelance"),
    path('buscar/',views.buscar),
    path('leerFreelance',views.leerFreelance,name='leerFreelance'),
    path('login',views.login_request, name="Login"),
    path('register', views.register, name='register'),
    
]

