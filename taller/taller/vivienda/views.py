from django.shortcuts import render

# Create your views here.
from vivienda.forms import *
from vivienda.models import *


def index(request):

    edificio = Edificio.objects.all()

    informacion_template = {'edificos': edificio}

    return render(request, 'index.html', informacion_template)

def crear_edficio(request):
    if request.method=='POST':
        formulario = EdificioForm(request.POST)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save() # se guarda en la base de datos
            return redirect(index)
    else:
        formulario = EdificioForm()
    diccionario = {'formulario': formulario}

    return render(request, 'crearEstudiante.html', diccionario)
    
    

