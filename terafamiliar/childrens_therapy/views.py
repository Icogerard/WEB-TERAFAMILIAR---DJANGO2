from django.shortcuts import render
from .models import Childrens_therapy

# Create your views here.
def childrens_therapy(request):
    childrens_therapies = Childrens_therapy.objects.all()
    return  render(request, "childrens_therapy/childrens_therapy.html", {'childrens_therapies':childrens_therapies})