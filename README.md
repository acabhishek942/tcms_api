To run the TCMS API service please follow the below steps.

Clone this repo

```
cd tcms_api
python -m venv <path-to-venv>
source <path-to-venv>/bin/activate
pip install -r requirements.txt

python manage.py makemigrations
python manage.py migrate

python manage.py runserver
```


This web service is built using Django Web Framework and uses Django Rest Framework for simplifying creation of REST endpoints


Endpoint for registering new customers
```
curl --location 'http://127.0.0.1:8000/tcms-api/customers/register/' \
--header 'Content-Type: application/json' \
--data-raw '{
  "name": "John Doe",
  "date_of_birth": "1990-01-01",
  "email": "johndoe242@example.com",
  "aadhar_number": "123456789030",
  "phone_number": "1234567838",
  "current_plan": null,
  "plan_activation_date": null,
  "plan_status": false
}'

```


Endpoint for updating plan. This single endpoint will take care of renew plan, update plan and add new plan for a customer requirements
```
curl --location --request PATCH 'http://127.0.01:8000/tcms-api/customers/2/update-plan/' \
--header 'Content-Type: application/json' \
--data '{
    "current_plan": 2,
    "plan_activation_date": "2024-04-01",
    "plan_status": true
}'
```


Endpoint for fetching all customers 
```
curl --location 'http://127.0.01:8000/tcms-api/customers'
```
