from django.shortcuts import render
from .models import Teenagers_therapy

# Create your views here.
def teenagers_therapy(request):
    teenagers_therapies = Teenagers_therapy.objects.all()
    return  render(request, "teenagers_therapy/teenagers_therapy.html", {'teenagers_therapies':teenagers_therapies})