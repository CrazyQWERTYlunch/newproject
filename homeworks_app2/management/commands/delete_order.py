from django.core.management.base import BaseCommand
from homeworks_app2.models import Order


class Command(BaseCommand):
    help = 'Deletes order by id'

    def add_arguments(self, parser):
        parser.add_argument('id', type=int, help='Order id')


    def handle(self, *args, **kwargs):
        pk = kwargs['id']

        order = Order.objects.filter(pk=pk).first()

        order.delete()
        self.stdout.write(f'Deleted order {order}')



