from django.urls import path 
from App1 import views 

urlpatterns=[

    path('', views.inicio, name="Inicio"),
    path('Acceso', views.Acceso, name='Acceso'),
    path('Freelance', views.Freelance, name='Freelance'),
    path('Contratador', views.Contratador, name='Contratador'),
    path('Servicios', views.Servicios, name='Servicios'),
    path('freelanceFormulario', views.freelanceFormulario, name="freelanceFormulario"),
    path('contratadorFormulario', views.contratadorFormulario, name="contratadorFormulario"),
    path('busquedaFreelance',views.busquedaFreelance,name="busquedaFreelance"),
    path('buscar/',views.buscar),
]

