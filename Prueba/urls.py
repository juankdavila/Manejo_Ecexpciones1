from django.urls import path
from . import views

urlpatterns = [
    path('procesar/', views.procesar_numero, name='procesar_numero'),
]