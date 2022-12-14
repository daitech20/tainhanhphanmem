# Generated by Django 4.0.4 on 2022-05-08 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DataTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=10, unique=True)),
                ('image', models.ImageField(upload_to='images/')),
                ('key_word', models.CharField(max_length=100)),
                ('prioritize', models.IntegerField(default=0, unique=True)),
                ('prioritize_quantity', models.IntegerField(default=1)),
                ('key_default', models.CharField(default='Thường', max_length=20)),
                ('hits', models.IntegerField(default=0)),
                ('hits_today', models.IntegerField(default=0)),
                ('status', models.IntegerField(choices=[(0, 'Không hoạt động'), (1, 'Hoạt động')], default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Program',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('slug', models.SlugField(max_length=120, unique=True)),
                ('image', models.ImageField(upload_to='images/')),
                ('link', models.CharField(default='', max_length=255)),
            ],
        ),
    ]
