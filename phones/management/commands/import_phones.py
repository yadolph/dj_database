import csv
import re
from datetime import datetime
from django.template.defaultfilters import slugify
from django.core.management.base import BaseCommand
from phones.models import Phone


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        Phone.objects.all().delete()
        with open('phones.csv') as f:
            phones = csv.DictReader(f, delimiter=';')
            for row in phones:
                phone = Phone()
                phone.id = row['id']
                phone.name = row['name']
                phone.image = row['image']
                phone.lte_exists = row['lte_exists']
                phone.price = re.sub('[^0-9]', '', row['price'])
                phone.release_date = datetime.strptime(row['release_date'], '%Y-%m-%d')
                phone.slug = slugify(row['name'])
                phone.save()
            if Phone.objects.all():
                print('Импорт прошел успешно')
            else:
                print('Что-то пошло не так')
