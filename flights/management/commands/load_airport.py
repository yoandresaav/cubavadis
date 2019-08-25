# -*- coding: utf-8 -*-
import os
import csv
from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from django.db import transaction

from ...utils import create_airport

AIRPORT_CSV = 'airports.csv'
DIR_BULKDATA = 'bulkdata'
BASE_DIR = settings.BASE_DIR

FINAL_PATH = os.path.join(BASE_DIR, DIR_BULKDATA, AIRPORT_CSV)


class Command(BaseCommand):
    help = 'Load data for Airport'

    @transaction.atomic
    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Loading airport'))
        with open(FINAL_PATH, 'r') as csv_file:
            reader = csv.reader(csv_file)
            next(reader)  # skip header
            for row in reader:
                create_airport(row)
        self.stdout.write(self.style.SUCCESS('Successfully closed poll'))
