# Generated by Django 4.0.4 on 2022-09-10 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('keywords', '0007_alter_datatable_keyword'),
    ]

    operations = [
        migrations.AddField(
            model_name='program',
            name='content',
            field=models.TextField(default='', null=True),
        ),
    ]
