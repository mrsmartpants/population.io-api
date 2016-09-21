from django.core.management.base import BaseCommand


class Command(BaseCommand):
    args = ''
    help = 'Initiates pickles'

    def handle(self, *args, **kwargs):
        import api.algorithms
