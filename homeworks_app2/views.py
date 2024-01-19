from django.shortcuts import render, HttpResponse
from homeworks_app2.models import Client, Product, Order


def clients_view(request):
    clients = Client.objects.all()

    res_str = '<br>'.join([str(client) for client in clients])

    return HttpResponse(res_str)


def products_view(request):
    products = Product.objects.all()

    res_str = '<br>'.join([str(product) for product in products])

    return HttpResponse(res_str)

def orders_view(request):
    orders = Order.objects.all()
    res_str = ''
    for order in orders:
        prod = " ".join(map(str, order.product.all()))
        res_str += f'{order} : {prod} <br>'

    return HttpResponse(res_str)