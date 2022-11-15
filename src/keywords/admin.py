from django.contrib import admin
from .models import DataTable, Program, IpAddressUser
from projects.models import Project
import threading
import time
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.

class ProjectInline(admin.TabularInline):
    model = Project.keywords.through

class DataTableAdmin(admin.ModelAdmin):
    list_display = ('code', 'keyword', 'keyword_type', 'project_name', 'image', 'prioritize', 'prioritize_quantity','hits', 'hits_today', 'status')
    list_filter = ('code', 'keyword_type', 'project_name', 'status')
    exclude = ('prioritize_quantity_temp', 'hits', 'hits_today')
    readonly_fields = ('project_name',)
    inlines = [
        ProjectInline,
    ]
    def save_model(self, request, obj, form, change):
        print(obj.keyword)

        super(DataTableAdmin, self).save_model(request, obj, form, change)

        def reset_project_name():
            time.sleep(0.5)
            for datatable in DataTable.objects.all():
                print(datatable.projects.all())
                list_projects = list(datatable.projects.all())
                name = ''
                for pj in list_projects:
                    name = name + ' ' + pj.name
                datatable.project_name = name
                datatable.save()
        def update_name_projects():
            time.sleep(0.5)
            name = ''
            for pj in obj.projects.all():
                name = name + ' ' + pj.name
            obj.project_name = name
            obj.save() 

	#t1 = threading.Thread(target=reset_project_name)
        #t1.start()
        update_name_projects()
	#reset_project_name()
        #time.sleep(0.1)

class ProgramAdmin(SummernoteModelAdmin):
    list_display = ('name', 'slug', 'image', 'keyword_type','link')
    summernote_fields = ('content',)

# class ProgramAdmin(admin.ModelAdmin):
#    list_display = ('name', 'slug', 'image', 'keyword_type','link')

class IpAddressUserAdmin(admin.ModelAdmin):
    list_display = ('ip', 'access', 'entered_password', 'time',)
    list_filter = ('access', 'entered_password', 'time',)

admin.site.register(DataTable, DataTableAdmin)
admin.site.register(Program, ProgramAdmin)
admin.site.register(IpAddressUser, IpAddressUserAdmin)
