from django.urls import path
from .views import inicio

urlpatterns = [
    path('', inicio, name='Hola_App'),

    ]