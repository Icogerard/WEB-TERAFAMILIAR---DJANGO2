from django.shortcuts import render
from .models import Couple_therapy

# Create your views here.
def couple_therapy(request):
    couples_therapies = Couple_therapy.objects.all()
    return  render(request, "couple_therapy/couple_therapy.html", {'couples_therapies':couples_therapies})