# Generated by Django 4.2.11 on 2024-03-17 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tcms_app', '0002_alter_customer_aadhar_number_alter_customer_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='plan_activation_date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
