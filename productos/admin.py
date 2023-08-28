from django.contrib import admin
from .models import productos
# Register your models here.

class productos_produc(admin.ModelAdmin):
    list_display = ('name','description','marca','stock', 'is_available')
    readonly_fields = ('create','cambio')
    ordering = ('marca',)
    list_filter= ('name','stock')
    prepopulated_fields = {'slug': ('name',)}



# falta la vista del administrador
admin.site.register(productos,productos_produc)