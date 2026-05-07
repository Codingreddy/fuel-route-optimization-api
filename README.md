A scalable and efficient REST API built using Django
 and Django REST Framework
 that calculates the most fuel-efficient truck route between two locations.

The API estimates:

Route distance
Fuel consumption
Fuel cost
Optimal fuel stops along the route
Features

✅ Calculate route distance between source and destination
✅ Estimate total fuel required
✅ Find nearby fuel stations along the route
✅ Calculate estimated fuel expenses
✅ Return optimized fuel stop suggestions
✅ PostgreSQL database integration
✅ CSV fuel station data import
✅ RESTful API architecture

Tech Stack
Technology	Purpose
Python 3
	Programming Language
Django
	Backend Framework
Django REST Framework
	REST API Development
PostgreSQL
	Database
Pandas
	CSV Processing
Geopy
	Geolocation Calculations
OpenRouteService API
	Route & Distance Calculation
Gunicorn
	Deployment Server
Project Structure
fuel_route_project/
│
├── config/
│   ├── settings.py
│   ├── urls.py
│
├── fuel/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│
├── manage.py
├── requirements.txt
├── fuel-prices.csv
└── README.md
Installation & Setup
1. Clone Repository
git clone https://github.com/Codingreddy/fuel-route-optimization-api.git
cd fuel-route-optimization-api
2. Create Virtual Environment
Mac/Linux
python3 -m venv venv
source venv/bin/activate
Windows
python -m venv venv
venv\Scripts\activate
3. Install Dependencies
pip install django djangorestframework psycopg2-binary pandas geopy requests python-dotenv gunicorn
PostgreSQL Setup
Install PostgreSQL

Download PostgreSQL:

PostgreSQL Download

Create Database

Open pgAdmin and create a database:

Database Name: fueldb
Configure Django Database

Open:

config/settings.py

Replace the DATABASES section:

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'fueldb',
        'USER': 'postgres',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
Add Installed Apps

Inside config/settings.py

INSTALLED_APPS = [
    ...
    'rest_framework',
    'fuel',
]
Run Database Migrations
python manage.py makemigrations
python manage.py migrate
Fuel Station Model

File:

fuel/models.py
from django.db import models

class FuelStation(models.Model):
    truckstop_name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    retail_price = models.FloatField()
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return self.truckstop_name
Import CSV Fuel Data

Place fuel-prices.csv inside the project root folder.

Open Django shell:

python manage.py shell

Run:

import pandas as pd
from fuel.models import FuelStation

df = pd.read_csv("fuel-prices.csv")

for _, row in df.iterrows():
    FuelStation.objects.create(
        truckstop_name=row['Truckstop Name'],
        city=row['City'],
        state=row['State'],
        retail_price=row['Retail Price'],
        latitude=row['Latitude'],
        longitude=row['Longitude']
    )
API Development
Create API View

File:

fuel/views.py

The API performs:

Route calculation
Fuel optimization
Fuel stop suggestions
Fuel cost estimation
URL Configuration
fuel/urls.py
from django.urls import path
from .views import RouteAPIView

urlpatterns = [
    path('route/', RouteAPIView.as_view()),
]
config/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('fuel.urls')),
]
Run Development Server
python manage.py runserver

Server URL:

http://127.0.0.1:8000/
API Endpoint
POST /api/route/
Sample Request
{
    "start": "Dallas",
    "destination": "Chicago"
}
Sample Response
{
    "start": "Dallas",
    "destination": "Chicago",
    "route_distance_miles": 966.4,
    "fuel_needed_gallons": 96.64,
    "total_fuel_cost": 406.77,
    "fuel_stops": [
        {
            "truckstop_name": "7-ELEVEN #218",
            "city": "Dallas",
            "state": "TX",
            "retail_price": 4.21
        }
    ]
}
Assumptions
Truck mileage = 10 MPG
Fuel prices are loaded from CSV dataset
Route data fetched using OpenRouteService API
Future Improvements
JWT Authentication
Docker Deployment
Redis Caching
Google Maps Integration
Advanced Route Optimization
Swagger API Documentation
CI/CD Pipeline
Run Tests
python manage.py test
Deployment

Production deployment can be done using:

Gunicorn
Render
Railway
AWS EC2
API Workflow
User Request
     ↓
Route Calculation
     ↓
Fuel Consumption Estimation
     ↓
Nearby Fuel Station Search
     ↓
Cost Optimization
     ↓
JSON API Response
Author
Hemanth Reddy

Backend Developer | Django Developer | Python Enthusiast
