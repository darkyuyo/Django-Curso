from django.contrib import admin
from .models import AutorModel,FraseModel,Profesion
# Register your models here.

admin.site.site_header = "Administración de Autores y Frases"
admin.site.index_title = "Administración de Autores y Frases 2"

class FraseInLine(admin.TabularInline):
    model = FraseModel
    extra = 1

@admin.register(Profesion)
class ProfesionAdmin(admin.ModelAdmin):
    list_display = ["nombre"]
    fields = ["nombre"]

class AutorAdmin(admin.ModelAdmin):
    fields = ["nombre","fecha_nacimiento","fecha_fallecimiento","profesion","nacionalidad"]
    list_display = ["nombre","fecha_nacimiento","fecha_fallecimiento","nacionalidad"]
    search_fields = ["nombre","profesion","nacionalidad"]
    list_filter = ["profesion","nacionalidad"]
    list_per_page = 5
    inlines = [FraseInLine]

    def actualizar_o(self,request,queryset):
        for obj in queryset:
            if "O" in obj.nombre:
                obj.nombre = obj.nombre.replace("O","o")
                obj.save()
        self.message_user(request,"Se han actualizado los nombres")

    actualizar_o.short_description = "Actualizar letras o"

    actions=["actualizar_o"]

admin.site.register(AutorModel,AutorAdmin)

@admin.register(FraseModel)
class FraseAdmin(admin.ModelAdmin):
    fields = ["autor","cita"]
    list_display = ["autor","cita"]
    search_fields = ["autor","cita"]
    list_filter = ["autor"]
    list_per_page = 5
