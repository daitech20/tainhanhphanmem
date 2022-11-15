from django.contrib import admin
from .models import Project
from keywords.models import DataTable
from django.db.models.signals import m2m_changed
from django.dispatch import receiver
# Register your models here.

def update_name_projects():
    for datatable in DataTable.objects.all():
        list_projects = list(datatable.projects.all())
        name = ''
        for pj in list_projects:
            name = name + ' ' + pj.name

        datatable.project_name = name
        datatable.save()

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name',)

    def delete_queryset(self, request, queryset):
        queryset.delete()

        update_name_projects()


    def delete_model(self, request, obj):
        obj.delete()

        update_name_projects()

# admin.site.register(Project, ProjectAdmin)

@receiver(m2m_changed, sender=Project.keywords.through)
def my_handler(sender, **kwargs):
    action = kwargs.pop('action', None)
    update_name_projects()
