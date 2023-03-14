from django.contrib import admin

from .models import Order, OrderItem, ShippingAddress


class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'created_at', 'shipping_address', 'status',
                    'order_items', 'payment_method', 'total_price',)

    def order_items(self, obj):
        return [o for o in obj.items.all()]


class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('item', 'order', 'quantity', 'total_price',)


class ShippingAddressAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'email',
                    'phone', 'address_line_1', 'address_line_2',)


admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)
admin.site.register(ShippingAddress, ShippingAddressAdmin)
