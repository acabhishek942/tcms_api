from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Customer, TelecomPlan

class CustomerPlanUpdateAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.plan = TelecomPlan.objects.create(plan_name='Gold180', cost=299, validity=180)
        self.customer = Customer.objects.create(
            name='John Doe',
            date_of_birth='1990-01-01',
            email='johndoe@example.com',
            aadhar_number='123456789012',
            phone_number='9876543210',
            current_plan=None,  # Initially no plan assigned
        )
        self.valid_payload = {
            'current_plan': self.plan.id,
            'plan_activation_date': '2024-03-20',
            'plan_status': True,
            'id': self.customer.id,
        }
        self.invalid_payload = {
            'current_plan': 999,  # Invalid plan ID
            'plan_activation_date': '2024-03-20',
            'plan_status': True,
            'id': self.customer.id,
        }

    def test_update_customer_plan_valid_payload(self):
        response = self.client.patch(
            f'/tcms-api/customers/{self.customer.id}/update-plan/',
            self.valid_payload,
            format='json',
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.customer.refresh_from_db()
        self.assertEqual(self.customer.current_plan, self.plan)

    def test_update_customer_plan_invalid_payload(self):
        response = self.client.patch(
            f'/tcms-api/customers/{self.customer.id}/update-plan/',
            self.invalid_payload,
            format='json',
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
