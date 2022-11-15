from django.db import models
from keywords.models import DataTable, Program
from django.db import transaction

# Create your models here.

class Project(models.Model):
    name = models.CharField(max_length=20, unique=True)
    keywords = models.ManyToManyField(DataTable, related_name='projects')
    programs = models.ManyToManyField(Program)


    def __str__(self):
        return self.name
