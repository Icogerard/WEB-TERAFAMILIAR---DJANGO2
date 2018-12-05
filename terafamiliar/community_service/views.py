from django.shortcuts import render
from .models import Community_service

# Create your views here.
def community_service(request):
    community_services = Community_service.objects.all()
    return  render(request, "community_service/community_service.html", {'community_services':community_services})