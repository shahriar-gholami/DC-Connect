from django.urls import path
from .views import *

urlpatterns = [
    path('create-new-link/', CreateNewLinkAPIView.as_view(), name='create_new_link'),
]