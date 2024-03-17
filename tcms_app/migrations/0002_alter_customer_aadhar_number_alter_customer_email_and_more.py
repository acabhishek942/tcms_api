# Generated by Django 4.2.11 on 2024-03-17 14:55

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tcms_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='aadhar_number',
            field=models.CharField(max_length=12, unique=True, validators=[django.core.validators.MinLengthValidator(12)]),
        ),
        migrations.AlterField(
            model_name='customer',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='phone_number',
            field=models.CharField(max_length=10, unique=True, validators=[django.core.validators.MinLengthValidator(10)]),
        ),
        migrations.AlterField(
            model_name='customer',
            name='plan_status',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
