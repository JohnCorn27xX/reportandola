from django.contrib import admin
from .models import *


class ClienteAdmin(admin.ModelAdmin):
    search_fields=('nombre', )

admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Copiadora)
admin.site.register(Ubicacion)

class Equipo_SitioAdmin(admin.ModelAdmin):
    search_fields=('cliente__nombre', 'departamento', 'ubicacion__ciudad', 'copiadora__nombre')

admin.site.register(Equipo_Sitio, Equipo_SitioAdmin)


