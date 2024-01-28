from django.shortcuts import render
from homeworks_app3.models import Order, Product

def catalog(request):
    # Показать все имеющиеся товары
    products = Product.objects.all()

    context = {
        'title': 'Товары',
        'products': products,
    }
    return render(request, 'homeworks_app3/catalog.html', context=context)


def index(request):
    context = {
        'title': 'Home - Главная',
        'content': 'Это главная страница сайта',
    }
    return render(request, "homeworks_app3/index.html", context=context)


def get_orders(request):
    content = Order.objects.all()
    return render(request, "homeworks_app3/index.html", context={'content': content})
