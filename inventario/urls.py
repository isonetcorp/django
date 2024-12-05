from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r"categorias", views.CategoriaViewSet)
router.register(r"tipoGastos", views.TipoGastoViewSet)
router.register(r"proveedores", views.ProveedorViewSet)
router.register(r"gastos", views.GastoViewSet)

urlpatterns = [
    path('contact/<str:name>', views.contact),
    path('categorias/', views.categorias),
    path('proveedores/', views.proveedores),
    path('gastos/contador/', views.total_gastos),
    path('', include(router.urls))
]
