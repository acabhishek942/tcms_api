from django.urls import path
from . import views

urlpatterns = [
    path('customers/register/', views.CustomerRegistrationAPIView.as_view(), name='customer-register'),
    path('customers/', views.CustomerListAPIView.as_view(), name='customers'),
    path('customers/<int:pk>/update-plan/', views.CustomerPlanUpdateAPIView.as_view(), name='customer-plan-update')

    # Other URLs
]
