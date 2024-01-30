from django.contrib import admin
#
# from homeworks_app3.models import Client, Product, OrderItem, Order
#
#
# @admin.register(Client)
# class ClientAdmin(admin.ModelAdmin):
#     list_display = ['username', 'email', ]
#     search_fields = ['username', 'email', ]
#
#     # inlines = [CartTabAdmin, OrderTabulareAdmin,]
#
#
# @admin.register(Product)
# class ProductsAdmin(admin.ModelAdmin):
#     prepopulated_fields = {'slug': ('name',)}
#     list_display = ['name', 'quantity', 'price', 'discount']
#     list_editable = ['discount', ]
#     search_fields = ['name', 'description']
#     list_filter = ['discount', 'quantity', ]
#     fields = [
#         "name",
#         "slug",
#         "description",
#         # "image",
#         ("price"),
#         "quantity",
#     ]
#
# @admin.register(OrderItem)
# class OrderItemAdmin(admin.ModelAdmin):
#     list_display = "order", "product", "price", "quantity"
#     search_fields = (
#         "order",
#         "product",
#     )
#
#
# @admin.register(Order)
# class OrderAdmin(admin.ModelAdmin):
#     list_display = (
#         "id",
#         "client",
#         "requires_delivery",
#         "status",
#         "payment_on_get",
#         "is_paid",
#         "created_timestamp",
#     )
#     search_fields = (
#         "id",
#     )
#
#     # readonly_fields = ("created_timestamp",)
#
#     list_filter = (
#         "requires_delivery",
#         "status",
#         "payment_on_get",
#         "is_paid",
#         "created_timestamp",
#     )
#
#     # inlines = (OrderItemTabulareAdmin,)
