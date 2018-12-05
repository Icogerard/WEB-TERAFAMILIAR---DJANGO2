from django.urls import path
from . import views

urlpatterns = [
    path('', views.individual_therapy, name="individual_therapy"),
]