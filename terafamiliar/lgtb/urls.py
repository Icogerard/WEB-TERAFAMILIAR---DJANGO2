from django.urls import path
from . import views

urlpatterns = [
    path('', views.lgtb, name="lgtb"),
]