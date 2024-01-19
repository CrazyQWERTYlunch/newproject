from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя')
    email = models.EmailField(verbose_name='Почта')
    phone = models.CharField(max_length=15, verbose_name='Телефон')
    address = models.CharField(max_length=255, verbose_name='Адрес')
    date_reg = models.DateField(auto_now_add=True, verbose_name='Дата регистрации')

    def __str__(self):
        return f'Client {self.name} {self.email}'


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Цена')
    quantity = models.PositiveIntegerField(default=0, verbose_name='Количество')
    date_added = models.DateField(auto_now_add=True, verbose_name='Дата добавления')

    def __str__(self):
        return f'Product {self.name} {self.description}'


class Order(models.Model):
    client = models.ForeignKey(to=Client, on_delete=models.CASCADE, verbose_name='Клиент')
    product = models.ManyToManyField(to=Product, verbose_name='Продукт')
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name='Итоговая цена')
    date_order = models.DateTimeField(auto_now=True, verbose_name='Дата оформления заказа')

    def __str__(self):
        return f'Order {self.client.name} {self.total_price}'

    def __repr__(self):
        return f'{self.client}, {self.product}, {self.total_price}, {self.date_order}'
