from django.contrib import admin
from .models import Producto
from .models import Categoria
from .models import TipoGasto
from .models import Proveedor
from .models import Gasto


class CategoriaAdmin(admin.ModelAdmin):
       search_fields = ('nombre',)
       list_display = ('nombre',)


class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'categoria', 'precio', 'stock', 'disponible')
    ordering = ('nombre',)
    search_fields = ('nombre',)
    list_filter = ('disponible','categoria',)
    
class ProveedorAdmin(admin.ModelAdmin):
    search_fields = ('nombre_proveedor',)
    list_display = ('nombre_proveedor','direccion',)
    
  

admin.site.register(Producto, ProductoAdmin)
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Proveedor, ProveedorAdmin)
admin.site.register(TipoGasto)
admin.site.register(Gasto)

