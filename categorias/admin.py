from django.contrib import admin
from .models import categoria
# Register your models here.

class categoryAdmin(admin.ModelAdmin):
    list_display = ('name_category','description')
    list_filter = ('name_category','created')
    ordering = ('name_category',)
    prepopulated_fields = {'slug': ('name_category',)}
# falta la vista del administrador
admin.site.register(categoria,categoryAdmin)