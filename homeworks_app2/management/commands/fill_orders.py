from django.core.management.base import BaseCommand
from homeworks_app2.models import Order, Client, Product


class Command(BaseCommand):
    help = 'Creates new order'

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Number of new orders')

    def handle(self, *args, **kwargs):
        count = kwargs['count']

        clients = Client.objects.all()

        for i in range(0, count):
            client = clients[i]

            order = Order(
                client=client,
            )

            self.stdout.write(f'Create {order} {order.total_price}')
            order.save()

