from django.shortcuts import render
from .models import Lgtb

# Create your views here.
def lgtb(request):
    lgtbs = Lgtb.objects.all()
    return  render(request, "lgtb/lgtb.html", {'lgtbs':lgtbs})
    