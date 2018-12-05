from django.urls import path
from . import views

urlpatterns = [
    path('', views.teenagers_therapy, name="teenagers_therapy"),
]