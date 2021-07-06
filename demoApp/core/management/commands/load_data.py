import os
import json

from forex_python.converter import CurrencyRates, CurrencyCodes

from django.core.management.base import BaseCommand, CommandError

from core.models import Currency


def load_currency():
    print("Adding currencies..")
    currencies = CurrencyRates()
    code = CurrencyCodes()
    for key in currencies.get_rates('USD').keys():
        symbol = code.get_symbol(key)
        Currency.objects.get_or_create(name=key, symbol=symbol)
    print("Done..")


class Command(BaseCommand):

    def handle(self, *args, **options):
        load_currency()
