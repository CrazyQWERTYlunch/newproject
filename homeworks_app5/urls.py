from django.urls import path

from homeworks_app5 import views
app_name = 'homeworks_app5'

urlpatterns = [
    path('', views.index, name='index'),
    # path('get_orders/', views.get_orders, name='get_orders'),
#     path('orders_view/', orders_view, name='orders_view'),
]
