from django.shortcuts import render

# Create your views here.
from vivienda.forms import *
from vivienda.models import *
from django.shortcuts import redirect

def index(request):

    edificio = Edificio.objects.all()

    informacion_template = {'edificios': edificio}

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

    return render(request, 'crearEdificio.html', diccionario)
    
def crear_departamento(request):
    if request.method=='POST':
        formulario = DeparatmentoForm(request.POST)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save() # se guarda en la base de datos
            return redirect(index)
    else:
        formulario = DeparatmentoForm()
    diccionario = {'formulario': formulario}

    return render(request, 'crearDepartamento.html', diccionario)

def editar_Edificio(request, id):

    edificio = Edificio.objects.get(pk=id)
    if request.method=='POST':
        formulario = EdificioForm(request.POST, instance=edificio)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()
            return redirect(index)
    else:
        formulario = EdificioForm(instance=edificio)
    diccionario = {'formulario': formulario}

    return render(request, 'editarEdificio.html', diccionario)

def eliminar_edificio(request, id):
    """
    """
    edificio = Edificio.objects.get(pk=id)
    edificio.delete()
    return redirect(index)

def editar_Departamento(request, id):
    departamento = Departamento.objects.get(pk=id)
    if request.method=='POST':
        formulario = DeparatmentoForm(request.POST, instance=departamento)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()
            return redirect(index)
    else:
        formulario = DeparatmentoForm(instance=departamento)
    diccionario = {'formulario': formulario}

    return render(request, 'editarDepartamento.html', diccionario)

def obtener_edificios(request, id):

    edificio = Edificio.objects.get(pk=id)
    informacion_template = {'edificios': edificio}
    return render(request, 'listado_edificio.html', informacion_template)

def obtener_departamentos(request, id):

    departamento = Departamento.objects.get(pk = id)
    informacion_template = {'departamentos': departamento}
    return render(request, 'listado_departamento.html', informacion_template)

def eliminar_departamento(request, id):
    """
    """
    departamento = Departamento.objects.get(pk=id)
    departamento.delete()
    return redirect(index)



