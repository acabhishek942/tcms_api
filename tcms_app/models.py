from django.db import models
from django.core.validators import MinLengthValidator



class TelecomPlan(models.Model):
    class NameChoices(models.TextChoices):
        PLATINUM = "1", "Platinum365"
        GOLD = "2", "Gold180"
        SILVER = "3", "Silver90"
    class CostChoices(models.IntegerChoices):
        PLATINUM = 1, "Plan_499"
        GOLD = 2, "Plan_299"
        SILVER = 3, "Plan_199"
    class ValidityChoices(models.IntegerChoices):
        PLATINUM = 1, "Validity_365"
        GOLD = 2, "Validity_180"
        SILVER = 3, "Validity_90"
    plan_name = models.CharField(max_length=20, choices=NameChoices.choices)
    cost = models.IntegerField(choices=CostChoices.choices)
    validity = models.IntegerField(choices=ValidityChoices.choices)

class Customer(models.Model):
    name = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    email = models.EmailField(unique=True)
    aadhar_number = models.CharField(unique=True, max_length=12, validators=[MinLengthValidator(12)])
    registration_date = models.DateField(auto_now_add=True)
    phone_number = models.CharField(unique=True, max_length=10, validators=[MinLengthValidator(10)])
    current_plan = models.ForeignKey(TelecomPlan, blank=True, null=True, on_delete=models.SET_NULL)
    plan_activation_date = models.DateField(null=True, auto_now=True)
    plan_status = models.BooleanField(default=False, null=True)