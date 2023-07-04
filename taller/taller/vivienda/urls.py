"""
    Manejo de urls para la aplicación
    administrativo
"""
from django.urls import path
# se importa las vistas de la aplicación
from . import views


urlpatterns = [
        path('', views.index, name='index'),
        path('crear/edificio', views.crear_edficio, name = 'crear_edificio'),
        path('crear/departameto', views.crear_departamento, name = 'crear_departamento'),
        path('editar_edificio/<int:id>', views.editar_Edificio, name = 'editar_edificio'),
        path('eliminar_edificio/<int:id>', views.eliminar_edificio, name = 'eliminar_edificio'),
        path('editar_departamento/<int:id>', views.editar_Departamento, name = 'editar_departamento'),
        path('listado_edificios/<int:id>', views.obtener_edificios, name= 'listado_edificios'),
        path('listado_departamento/<int:id>', views.obtener_departamentos, name= 'listado_departamento'),
        path('eliminar_departamento/<int:id>', views.eliminar_departamento, name = 'eliminar_departamento'),


 ]