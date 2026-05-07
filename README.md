# Fuel Route Optimization API

A Django REST API that calculates the optimal fuel stops between two locations for a truck route.

The API:
- Calculates route distance
- Estimates fuel required
- Finds fuel stations along the route
- Calculates total fuel cost
- Returns optimized fuel stop suggestions

---

# Technologies Used

| Technology | Purpose |
|------------|---------|
| Python 3 | Programming Language |
| Django | Backend Framework |
| Django REST Framework | API Development |
| PostgreSQL | Database |
| Pandas | CSV Data Import |
| OpenRouteService API | Route Distance & Directions |
| Geopy | Geolocation |
| Gunicorn | Deployment Server |

---

# Project Setup (Step-by-Step)

## 1. Install Python

Download Python from:

https://www.python.org/downloads/

Verify installation:
python3 --version

2. Install PostgreSQL

Download PostgreSQL:

https://www.postgresql.org/download/

Open pgAdmin and create database:

Database Name: fueldb

3. Create Project Folder
mkdir fuel_route_project
cd fuel_route_project

4. Create Virtual Environment
python3 -m venv venv

Activate virtual environment:

Mac/Linux
source venv/bin/activate
Windows
venv\Scripts\activate
5. Install Dependencies
pip install django djangorestframework psycopg2-binary pandas geopy requests python-dotenv
6. Create Django Project
django-admin startproject config .

Create app:

python manage.py startapp fuel
7. Configure PostgreSQL

Open:

config/settings.py

Replace DATABASES section:

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
8. Add Installed Apps

In settings.py:

INSTALLED_APPS = [
    ...
    'rest_framework',
    'fuel',
]
9. Run Migrations
python manage.py makemigrations
python manage.py migrate
10. Create FuelStation Model

Inside:

fuel/models.py

Example fields:

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
11. Import CSV Data

Place CSV file inside project folder.

Create import script:

python manage.py shell

Example:

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
12. Create API View

Inside:

fuel/views.py

Create API endpoint for:

route calculation
fuel optimization
nearest fuel stations
13. Configure URLs
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
14. Run Server
python manage.py runserver

Server runs at:

http://127.0.0.1:8000/
API Endpoint
POST Request
/api/route/
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
Fuel prices are taken from CSV dataset
Route calculated using OpenRouteService API
Future Improvements
JWT Authentication
Docker Deployment
Redis Caching
Google Maps Integration
Advanced Route Optimization
Run Tests
python manage.py test
Author

Hemanth Reddy
