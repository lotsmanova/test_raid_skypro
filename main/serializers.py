from rest_framework.serializers import ModelSerializer

from main.models import FrameworkModel


class FrameworkListSerializer(ModelSerializer):
    class Meta:
        model = FrameworkModel
        fields = '__all__'
