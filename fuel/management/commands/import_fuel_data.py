import csv
import os

from django.conf import settings
from django.core.management.base import BaseCommand

from fuel.models import FuelStation


class Command(BaseCommand):
    help = "Import fuel station CSV data"

    def handle(self, *args, **kwargs):

        csv_path = os.path.join(
            settings.BASE_DIR,
            'fuel',
            'data',
            'fuel_stations.csv'
        )

        with open(csv_path, newline='', encoding='utf-8') as csvfile:

            reader = csv.DictReader(csvfile)

            for row in reader:

                FuelStation.objects.create(
                    truckstop_name=row['truckstop_name'],
                    address=row['address'],
                    city=row['city'],
                    state=row['state'],
                    retail_price=float(row['retail_price']),
                )

        self.stdout.write(
            self.style.SUCCESS('CSV data imported successfully!')
        )