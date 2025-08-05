from django.urls import path, include
from .views import *

app_name = "info"

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
]