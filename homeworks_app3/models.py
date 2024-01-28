from django.db import models
from django.contrib.auth.models import AbstractUser


class UpdateQueryset(models.QuerySet):
    def total_price(self):
        return sum(cart.products_price() for cart in self)

    def total_quantity(self):
        if self:
            return sum(cart.quantity for cart in self)
        return 0


class Client(AbstractUser):
    phone_number = models.CharField(max_length=10, blank=True, null=True, verbose_name='Номер телефона')
    address = models.CharField(max_length=255, blank=True, null=True, verbose_name='Адрес')

    class Meta:
        db_table = 'user'
        verbose_name = 'Пользователя'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return f'Client {self.username} {self.email}'


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Цена')
    quantity = models.PositiveIntegerField(default=0, verbose_name='Количество')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    discount = models.DecimalField(default=0.00, max_digits=4, decimal_places=2, verbose_name='Скидка в %')
    image = models.ImageField(upload_to='goods_images', blank=True, null=True, verbose_name='Изображение')
    date_added = models.DateField(auto_now_add=True, verbose_name='Дата добавления')

    class Meta:
        db_table = 'product'
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ('id', )

    def __str__(self) -> str:
        return f'{self.name} Количество - {self.quantity}'

    def sell_price(self):
        if self.discount:
            return round(self.price - self.price * self.discount / 100, 2)
        return self.price


class Cart(models.Model):
    # Промежуточная зона, набирание продуктов в заказ, аналогия OrderItem, но без привязки к классу Order
    client = models.ForeignKey(to=Client, on_delete=models.CASCADE, verbose_name='Пользователь')
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE, verbose_name='Товар')
    quantity = models.PositiveSmallIntegerField(default=0, verbose_name='Количество')
    created_timestamp = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')

    class Meta:
        db_table = 'cart'
        verbose_name = "Корзина"
        verbose_name_plural = "Корзина"

    objects = UpdateQueryset().as_manager()

    def products_price(self):
        return round(self.product.sell_price() * self.quantity, 2)

    def __str__(self):
        return f'Корзина {self.client.username} | Товар {self.product.name} | Количество {self.quantity}'


class Order(models.Model):
    client = models.ForeignKey(to=Client, on_delete=models.CASCADE, verbose_name='Клиент')
    created_timestamp = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания заказа")
    phone_number = models.CharField(max_length=20, verbose_name="Номер телефона")
    requires_delivery = models.BooleanField(default=False, verbose_name="Требуется доставка")
    delivery_address = models.TextField(null=True, blank=True, verbose_name="Адрес доставки")
    payment_on_get = models.BooleanField(default=False, verbose_name="Оплата при получении")
    is_paid = models.BooleanField(default=False, verbose_name="Оплачено")
    status = models.CharField(max_length=50, default="В обработке", verbose_name="Статус заказа")

    def __str__(self) -> str:
        return f'Заказ № {self.pk} | Покупатель {self.client.first_name} {self.client.last_name}'


class OrderItem(models.Model):
    order = models.ForeignKey(to=Order, on_delete=models.CASCADE, verbose_name="Заказ")
    product = models.ForeignKey(to=Product, on_delete=models.SET_DEFAULT, null=True, verbose_name="Продукт",
                                default=None)
    name = models.CharField(max_length=150, verbose_name="Название")
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Цена")
    quantity = models.PositiveIntegerField(default=0, verbose_name="Количество")
    created_timestamp = models.DateTimeField(auto_now_add=True, verbose_name="Дата продажи")

    objects = UpdateQueryset.as_manager()

    class Meta:
        db_table = "order_item"
        verbose_name = "Проданный товар"
        verbose_name_plural = "Проданные товары"

    def products_price(self):
        return round(self.price * self.quantity, 2)

    def __str__(self) -> str:
        return f'Заказ № {self.order.pk} | Товар {self.name}'
