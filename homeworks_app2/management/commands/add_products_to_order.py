from django.core.management.base import BaseCommand
from homeworks_app2.models import Order, Product

class Command(BaseCommand):
    help = 'Add product to the order'

    def add_arguments(self, parser):
        parser.add_argument('id', type=int, help='Order ID')

    def handle(self, *args, **kwargs):
        pk = kwargs['id']

        order = Order.objects.filter(pk=pk).first()
        order.product.add(*Product.objects.all())

        order.total_price = sum(map(lambda x: x.price, order.product.all()))

        self.stdout.write(f'Edits {order} {order.total_price}')
        order.save()