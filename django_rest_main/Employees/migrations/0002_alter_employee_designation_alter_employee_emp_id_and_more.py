# Generated by Django 5.2.1 on 2025-05-31 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Employees', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='designation',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='employee',
            name='emp_id',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='employee',
            name='emp_name',
            field=models.CharField(max_length=30),
        ),
    ]
