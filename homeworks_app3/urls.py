from django.urls import path

from homeworks_app3 import views
app_name = 'homeworks_app3'

urlpatterns = [
    path('', views.index, name='index'),
    path('get_orders/', views.get_orders, name='get_orders'),
#     path('orders_view/', orders_view, name='orders_view'),
]
