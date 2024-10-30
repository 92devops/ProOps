# Generated by Django 3.2 on 2024-10-29 14:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Deparment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=32, verbose_name='部门名称')),
            ],
            options={
                'verbose_name': '部门',
                'verbose_name_plural': '部门',
                'db_table': 't_department',
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=32, verbose_name='姓名')),
                ('password', models.CharField(max_length=32, verbose_name='密码')),
                ('age', models.IntegerField(default=1, verbose_name='年龄')),
                ('gender', models.SmallIntegerField(choices=[(0, '女'), (1, '男')], default=0, verbose_name='性别')),
                ('salary', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='薪资')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='employee', to='department.deparment')),
            ],
            options={
                'verbose_name': '员工',
                'verbose_name_plural': '员工',
                'db_table': 't_employee',
            },
        ),
    ]