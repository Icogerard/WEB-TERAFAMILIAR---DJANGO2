from django.contrib import admin
from .models import Lgtb

# Register your models here.
class LgtbAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('title', 'published')
    orderig = ('title', 'published')
    search_fields = ('title',)
    date_hierarchy = 'published'
    list_filter = ('published',)

admin.site.register(Lgtb, LgtbAdmin)