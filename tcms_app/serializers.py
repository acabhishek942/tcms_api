from rest_framework import serializers
from .models import Customer

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id', 'name', 'date_of_birth', 'email', 'aadhar_number', 'registration_date', 'phone_number', 'current_plan', 'plan_activation_date', 'plan_status']

class CustomerPlanUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['current_plan', 'plan_activation_date', 'plan_status', 'id']
