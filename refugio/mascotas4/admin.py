from django.contrib import admin
from mascotas4.models import usuario_solicitud,Mascota,Vacunas
# Register your models here.
admin.site.register(usuario_solicitud)
admin.site.register(Mascota)
admin.site.register(Vacunas)