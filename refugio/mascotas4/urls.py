

from django.urls import path
from .views import ejemplo, listar_mascotas, mascota_edit, \
    ingreso_mascota, mascota_delete, ingreso_solicitud, listar_solicitudes, solicitud_edit, solicitud_delete
#mascotas4
urlpatterns = [
    
    path('verbarra/', ejemplo, name='index'),
    path('solicitud/', ingreso_solicitud, name='ingreso_solicitud'),
    path('versolicitudes/', listar_solicitudes, name='solicitud_listar'),
    path('editarsolicitud/<int:id>',solicitud_edit,name='solicitud_editar'),
    path('eiminarsolicitud/<int:id>',solicitud_delete,name='solicitud_eliminar'),

    path('registromascota/', ingreso_mascota,name='registro_mascota'),
    path('vermascotas/',listar_mascotas, name='mascota_listar'),
    path('editar/<int:id>',mascota_edit,name='mascota_editar'),
    path('eiminar/<int:id>',mascota_delete,name='mascota_eliminar'),

    ]