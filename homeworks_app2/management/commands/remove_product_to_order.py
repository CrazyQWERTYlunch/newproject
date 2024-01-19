from django.core.management.base import BaseCommand
from homeworks_app2.models import Order, Product

class Command(BaseCommand):
    help = 'Add product to the order'

    def add_arguments(self, parser):
        parser.add_argument('id', type=int, help='Order ID')
        parser.add_argument('prod_id', type=int, help='Product ID')

    def handle(self, *args, **kwargs):
        pk = kwargs['id']
        pk_prod = kwargs['prod_id']

        order = Order.objects.filter(pk=pk).first()
        product = Product.objects.filter(pk=pk_prod).first()
        order.product.remove(product)

        order.total_price = sum(map(lambda x: x.price, order.product.all()))

        self.stdout.write(f'Edits {order} {order.total_price}')
        order.save()