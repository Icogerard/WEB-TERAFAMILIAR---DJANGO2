from django.contrib import admin
from .models import Couple_therapy

# Register your models here.
class Couple_therapyAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('title', 'published')
    orderig = ('title', 'published')
    search_fields = ('title', 'subtitle',)
    date_hierarchy = 'published'
    list_filter = ('published',)

admin.site.register(Couple_therapy, Couple_therapyAdmin)