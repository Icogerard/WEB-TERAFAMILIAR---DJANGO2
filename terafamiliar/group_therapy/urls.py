from django.urls import path
from . import views

urlpatterns = [
    path('', views.group_therapy, name="group_therapy"),
]