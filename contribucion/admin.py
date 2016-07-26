from django.contrib import admin
from contribucion.models import Autor, Trabajo
# Register your models here.

class AutorAdmin(admin.ModelAdmin):
    list_display = ('orden', 'nombre','primer_apellido','segundo_apellido','correo', 'institucion')

class ContribucionAdmin(admin.ModelAdmin):
    list_display = ('registro', 'titulo', 'area_tematica')


admin.site.register(Autor, AutorAdmin)
admin.site.register(Trabajo,ContribucionAdmin)
