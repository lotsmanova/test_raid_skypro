from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework.generics import ListAPIView

from main.models import FrameworkModel
from main.serializers import FrameworkListSerializer


class FrameworkListAPIView(ListAPIView):
    queryset = FrameworkModel.objects.all()
    serializer_class = FrameworkListSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ('language', )
