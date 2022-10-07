import csv
from django.core.management.base import BaseCommand
from django.utils.text import slugify

from phones.models import Phone


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as file:
            phones = list(csv.DictReader(file, delimiter=';'))

        for phone in phones:
            # TODO: Добавьте сохранение модели
            if phone['lte_exists'] == 'True':
                lte = True
            else:
                lte = False
            # new_phone = Phone.objects.create(id=phone['id'], name=phone['name'], price=int(phone['price']), image=phone['image'], release_date=phone['release_date'], lte_exists=lte, slug=slugify(phone['name']))
            new_phone = Phone(id=phone['id'], name=phone['name'], price=int(phone['price']),
                                            image=phone['image'], release_date=phone['release_date'], lte_exists=lte,
                                            slug=slugify(phone['name']))
            new_phone.save()

