from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Ruta para football/
    path('datos/', views.get_odds, name='get_odds'),
]
