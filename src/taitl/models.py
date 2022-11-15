from django.db import models

STATUS = (
    (0, "Không hoạt động"),
    (1, "Hoạt động")
)


# Create your models here.
class DataTable(models.Model):
    code = models.CharField(max_length=10, unique=True)
    image = models.ImageField(upload_to='images/')
    key_word = models.CharField(max_length=100)
    prioritize = models.IntegerField(default=1)
    prioritize_quantity = models.IntegerField(default=0)
    prioritize_quantity_temp = models.IntegerField(default=0, null=True)
    key_default = models.CharField(max_length=20, default='Thường')
    hits = models.IntegerField(default=0)
    hits_today = models.IntegerField(default=0)
    status = models.IntegerField(choices=STATUS, default=0)


class Program(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=120, unique=True)
    image = models.ImageField(upload_to='images/')
    link = models.CharField(max_length=255, default='')