from django.urls import path
from . import views

urlpatterns = [
    path('', views.childrens_therapy, name="childrens_therapy"),
]