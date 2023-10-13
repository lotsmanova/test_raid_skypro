from rest_framework.generics import ListAPIView

from main.models import FrameworkModel
from main.serializers import FrameworkListSerializer


class FrameworkListAPIView(ListAPIView):
    queryset = FrameworkModel.objects.all()
    serializer_class = FrameworkListSerializer
