"""terafamiliar URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings

urlpatterns = [
    # Paths del core
    path('', include('core.urls')),
    # Paths de couple_therpay
    path('couple_therapy/', include('couple_therapy.urls')),
    # Paths de group_therapy
    path('group_therapy/', include('group_therapy.urls')),
    # Paths de childrens_therapy
    path('childrens_therapy/', include('childrens_therapy.urls')),
    # Paths de individual_therapy
    path('individual_therapy/', include('individual_therapy.urls')),
    # Paths de teenagers_therapy
    path('teenagers_therapy/', include('teenagers_therapy.urls')),
    # Paths de community_service
    path('community_service/', include('community_service.urls')),
    # Paths de testimonials
    path('testimonials/', include('testimonials.urls')),
    # Paths de contact
    path('contact/', include('contact.urls')),
    # Paths de lgbt+
    path('lgtb/', include('lgtb.urls')),


    #paths del admin
    path('admin/', admin.site.urls),
]

# Comprobamos si el DEBUG lo tenemos en marcha
if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# Custom titles for admin  
admin.site.site_header = "TERAFAMILIAR"
admin.site.index_title = "Administrar"
admin.site.site_title = "Terafamiliar Panel"