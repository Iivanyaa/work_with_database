import csv
from django.core.management.base import BaseCommand
from phones.models import Phone


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):

        with open('phones.csv', 'r', encoding='utf-8', errors='ignore') as file:
            phones = list(csv.DictReader(file, delimiter=';'))
            for phone in phones:
                phone_object = Phone(
                    id=phone['id'],
                    name=phone['name'],
                    price=phone['price'],
                    image=phone['image'],
                    release_date=phone['release_date'],
                    lte_exists=phone['lte_exists'],
                    slug=phone['name'].lower(),
                )
                phone_object.save()

        self.stdout.write(self.style.SUCCESS('Successfully imported phones'))               
