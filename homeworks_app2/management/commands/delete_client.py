from django.core.management.base import BaseCommand
from homeworks_app2.models import Client

class Command(BaseCommand):
    help = 'Deletes a client by id'

    def add_arguments(self, parser):
        parser.add_argument('id', type=int, help='Client id')

    def handle(self, *args, **kwargs):
        pk = kwargs['id']

        client = Client.objects.filter(pk=pk).first()

        client.delete()
        self.stdout.write(f'Deleted client {client}')
