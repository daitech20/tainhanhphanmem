from django.contrib import admin
from .models import DataTable, Program
import datetime

# Register your models here.
class DataTableAdmin(admin.ModelAdmin):
    list_display = ('code', 'key_word', 'image', 'prioritize', 'prioritize_quantity','hits', 'hits_today',  'key_default', 'status')
    exclude = ('prioritize_quantity_temp', 'hits', 'hits_today')

class ProgramAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'image', 'link')

admin.site.register(DataTable, DataTableAdmin)
admin.site.register(Program, ProgramAdmin)