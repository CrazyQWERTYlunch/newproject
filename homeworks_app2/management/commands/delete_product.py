from django.core.management.base import BaseCommand
from homeworks_app2.models import Product

class Command(BaseCommand):
    help = 'Deletes a product by id'

    def add_arguments(self, parser):
        parser.add_argument('id', type=int, help='Product id')

    def handle(self, *args, **kwargs):
        pk = kwargs['id']

        product = Product.objects.filter(pk=pk).first()

        product.delete()
        self.stdout.write(f'Deleted product {product}')