from django.shortcuts import render
from .models import Group_therapy

# Create your views here.
def group_therapy(request):
    group_therapies = Group_therapy.objects.all()
    return  render(request, "group_therapy/group_therapy.html", {'group_therapies':group_therapies})
    
