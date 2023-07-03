from django.shortcuts import render

# Create your views here.
from vivienda.forms import *

def index(self):

    edificio = Edificio.objects.all()
