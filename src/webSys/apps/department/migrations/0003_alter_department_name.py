# Generated by Django 3.2 on 2024-10-29 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('department', '0002_rename_deparment_department'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='name',
            field=models.CharField(max_length=32, unique=True, verbose_name='部门名称'),
        ),
    ]
