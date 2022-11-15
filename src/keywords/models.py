from django.db import models

STATUS = (
    (0, "Không hoạt động"),
    (1, "Hoạt động")
)

KEYWORD_TYPE = (
    (0, "Code Getlink"),
    (1, "Code Unzip")
)

# Create your models here.
class DataTable(models.Model):
    code = models.CharField(max_length=10)
    image = models.ImageField(upload_to='images/')
    image2 = models.ImageField(upload_to='images/')
    keyword = models.CharField(max_length=100)
    keyword_type = models.IntegerField(choices=KEYWORD_TYPE, default=0)
    project_name = models.CharField(max_length=512, null=True, blank=True)
    prioritize = models.IntegerField(default=1)
    prioritize_quantity = models.IntegerField(default=0)
    prioritize_quantity_temp = models.IntegerField(default=0, null=True)
    hits = models.IntegerField(default=0)
    hits_today = models.IntegerField(default=0)
    status = models.IntegerField(choices=STATUS, default=0)

    def __str__(self):
        return f'{self.code} + {self.keyword}'


class Program(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=120, unique=True)
    image = models.ImageField(upload_to='images/')
    keyword_type = models.IntegerField(choices=KEYWORD_TYPE, default=0)
    link = models.CharField(max_length=255, default='')
    pass_to_decompress = models.CharField(max_length=50, null=True, blank=True)
    content = models.TextField(null=True, default='')

    def __str__(self):
        return self.name


class IpAddressUser(models.Model):
    ip = models.CharField(max_length=20, unique=True)
    access = models.BooleanField()
    entered_password = models.BooleanField(default=False)
    time = models.DateTimeField(auto_now_add=True, blank=True)
