from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import newsweek

# Register your models here.
@admin.register(newsweek)


class ViewAdmin (ImportExportModelAdmin):
    list_display    = ('Title', 'slug', 'author', 'Points', 'publish', 'status')
    list_filter     = ('status', 'created', 'publish', 'author')
    search_fields   = ('Title', 'author')
    prepopulated_fields = {'slug':('Title',)}
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ('status', 'publish')
    pass



