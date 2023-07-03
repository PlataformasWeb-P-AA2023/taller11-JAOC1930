from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from django import forms

from vivienda import Edificio
from vivienda import Departamento

class EdificioForm(ModelForm):
    class meta:
        model: Edificio 
        fields = ['nonbre', 'direccion', 'ciudad', 'tipo']
        labels = {
            'nombre': _("Ingrese el nombre"),
            'direccion': _("Ingrese la direccion"),
            'ciudad': _("Ingrese la ciudad "),
            'tipo': _("Elija el tipo"),
        }


class DeparatmentoForm(ModelForm):
    class meta:
        model: Departamento
        fields = ['nombrePropietario', 'costo', 'num_cuartos', 'edificio']
        labels = {
            'nombrePropietario': _("Ingrese el nombre del propietario"),
            'costo': _("Ingrese el costo"),
            'num_cuartos': _("Ingrese el numero de cuartos"),
            'edificio': _("Elija el edifico"),

        }
