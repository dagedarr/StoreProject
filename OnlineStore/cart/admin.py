from django.contrib import admin

from .models import Cart, CartItem


class CartItemAdmin(admin.ModelAdmin):
    list_display = ('item', 'cart', 'quantity', 'total_price_field',)
    search_fields = ('item__title', 'cart__user__username',)
    list_filter = ('item', 'cart__user',)
    raw_id_fields = ('item', 'cart',)

    def total_price_field(self, obj):
        return obj.total_price

    total_price_field.short_description = 'Общая цена'


class CartAdmin(admin.ModelAdmin):
    list_display = ('user', 'created_at', 'cart_items', 'total_price_field',)
    list_filter = ('created_at',)
    search_fields = ('user__username', 'user__email', 'created_at',)
    readonly_fields = ('total_price',)

    def cart_items(self, obj):
        return [o for o in obj.items.all()]

    def total_price_field(self, obj):
        return obj.total_price

    cart_items.short_description = 'Список товаров'
    total_price_field.short_description = 'Общая цена'


admin.site.register(Cart, CartAdmin)
admin.site.register(CartItem, CartItemAdmin)
