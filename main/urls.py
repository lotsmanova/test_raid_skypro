from django.urls import path

from main.apps import MainConfig
from main.views import FrameworkListAPIView

app_name = MainConfig.name

urlpatterns = [
    path('frameworks/', FrameworkListAPIView.as_view(), name='framework_list'),
]
