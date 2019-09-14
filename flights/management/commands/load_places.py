# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand, CommandError
from django.db import transaction

from ...utils import load_places


class Command(BaseCommand):
    help = 'Load data for Airport'

    @transaction.atomic
    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Loading places'))
        load_places()
        self.stdout.write(self.style.SUCCESS('Successfully loaded places'))
