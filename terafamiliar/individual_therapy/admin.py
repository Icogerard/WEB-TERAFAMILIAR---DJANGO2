from django.contrib import admin
from .models import Individual_therapy

# Register your models here.
class Individual_therapyAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('title', 'published')
    orderig = ('title', 'published')
    search_fields = ('title', 'subtitle',)
    date_hierarchy = 'published'
    list_filter = ('published',)

admin.site.register(Individual_therapy, Individual_therapyAdmin)