

from django.urls import path
from .views import ejemplo, formulario_adopcion, ver_mascotas, mascota_edit, \
    Mascota_list, ingreso_mascota, MascotaCreate
#mascotas3
urlpatterns = [
    
    path('verbarra/', ejemplo, name='index'),
    path('registroMascota/', ingreso_mascota,name='regsitro_mascota'),
    path('vermascotas/',ver_mascotas, name='mascota_listar'),
    path('solicitud/', formulario_adopcion),
    path('editar/<int:id>',mascota_edit,name='mascota_editar'),

    ]