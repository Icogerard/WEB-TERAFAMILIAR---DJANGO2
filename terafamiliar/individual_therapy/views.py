from django.shortcuts import render
from .models import Individual_therapy

# Create your views here.
def individual_therapy(request):
    individual_therapies = Individual_therapy.objects.all()
    return  render(request, "individual_therapy/individual_therapy.html", {'individual_therapies':individual_therapies})