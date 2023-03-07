from django.contrib import admin

from .models import Cart, CartItem


class CartItemAdmin(admin.ModelAdmin):
    list_display = ('item', 'cart', 'quantity', 'total_price')


class CartAdmin(admin.ModelAdmin):
    list_display = ('user', 'created_at', 'cart_items', 'total_price')

    def cart_items(self, obj):
        return [o for o in obj.items.all()]


admin.site.register(Cart, CartAdmin)
admin.site.register(CartItem, CartItemAdmin)
