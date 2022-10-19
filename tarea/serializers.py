from rest_framework.serializers import ModelSerializer
from .models import Tarea


class TareaSerializer(ModelSerializer):
    class Meta:
        model = Tarea
        fields = '__all__'
