from django.core.management.base import BaseCommand
from homeworks_app2.models import Product


class Command(BaseCommand):
    help = 'Creates new product'

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Number of new products')

    def handle(self, *args, **kwargs):
        count = kwargs['count']

        for i in range(1, count):
            product = Product(
                name=f'Product{i}',
                description=f'Product{i} description.....',
                price=10.00,
                quantity=i
            )
            self.stdout.write(f'Create {product}')
            product.save()
