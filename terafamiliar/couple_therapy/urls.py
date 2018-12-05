from django.urls import path
from . import views

urlpatterns = [
    path('', views.couple_therapy, name="couple_therapy"),
]