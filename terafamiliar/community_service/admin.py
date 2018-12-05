from django.contrib import admin
from .models import Community_service

# Register your models here.
class Community_serviceAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('title', 'published')
    orderig = ('title', 'published')
    search_fields = ('title', 'subtitle',)
    date_hierarchy = 'published'
    list_filter = ('published',)

admin.site.register(Community_service, Community_serviceAdmin)