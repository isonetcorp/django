from rest_framework import serializers
from .models import Categoria
from .models import TipoGasto
from .models import Proveedor
from .models import Gasto

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = "__all__"


class TipoGastoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoGasto
        fields = "__all__"

class ProveedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proveedor
        fields = "__all__"

class GastoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gasto
        fields = "__all__"