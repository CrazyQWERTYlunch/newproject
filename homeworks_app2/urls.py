from django.urls import path

from homeworks_app2.views import clients_view, products_view, orders_view

app_name = 'homeworks_app1'

urlpatterns = [
    path('clients_view/', clients_view, name='clients_view'),
    path('products_view/', products_view, name='products_view'),
    path('orders_view/', orders_view, name='orders_view'),
]
