from django.contrib import admin

from .models import Order, OrderItem, ShippingAddress


class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'created_at', 'shipping_address', 'status',
                    'order_items', 'payment_method', 'total_price_field',)
    list_filter = ('status', 'payment_method',)
    search_fields = ('user__username', 'shipping_address__first_name', 'shipping_address__last_name',)
    date_hierarchy = 'created_at'

    def order_items(self, obj):
        return [o for o in obj.items.all()]

    def total_price_field(self, obj):
        return obj.total_price

    total_price_field.short_description = 'Общая цена'
    order_items.short_description = 'Список товаров'


class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('item', 'order', 'quantity', 'total_price_field',)
    list_filter = ('order__status',)
    search_fields = ('item__title', 'order__user__username',)

    def total_price_field(self, obj):
        return obj.total_price

    total_price_field.short_description = 'Общая цена'


class ShippingAddressAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'email',
                    'phone', 'address_line_1', 'address_line_2',)
    search_fields = ('first_name', 'last_name', 'email',)


admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)
admin.site.register(ShippingAddress, ShippingAddressAdmin)
