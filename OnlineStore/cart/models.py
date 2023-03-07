from django.db import models
from django.contrib.auth.models import User

from store.models import Item


class Cart(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='carts'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def total_price(self):
        return self.items.aggregate(
            models.Sum('item__price')
        )['item__price__sum']

    def __str__(self):
        return f"Cart {self.id} for {self.user.username}"


class CartItem(models.Model):
    cart = models.ForeignKey(
        Cart,
        on_delete=models.CASCADE,
        related_name='items'
    )
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    @property
    def total_price(self):
        total_price = self.quantity * self.item.price
        return total_price

    def __str__(self):
        return f"{self.quantity} x {self.item.title} in {self.cart}"
