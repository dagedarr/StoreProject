from django.db import models
from django.contrib.auth.models import User

from store.models import Item

class ShippingAddress(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address_line_1 = models.CharField(max_length=200)
    address_line_2 = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return f"""
        {self.address_line_1} {self.address_line_2}
        Для: {self.first_name} {self.last_name},
        Почта: {self.email},
        Телефон: {self.phone}
        """


class Order(models.Model):
    PAYMENT_METHOD_CHOICES = [
        ('cash_courier', 'Наличными курьеру'),
        ('card_courier', 'Картой курьеру'),
        ('card_online', 'Картой онлайн'),
    ]
    STATUS_CHOICES=[
        ('created', 'Создан'),
        ('processing', 'Обрабатывается'),
        ('shipped', 'Отправлен'),
        ('delivered', 'Доставлен'),
        ('canceled', 'Отменен'),
    ]
    payment_method = models.CharField(
        max_length=20,
        choices=PAYMENT_METHOD_CHOICES,
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    created_at = models.DateTimeField(auto_now_add=True)
    shipping_address = models.OneToOneField(ShippingAddress, on_delete=models.CASCADE)
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='created',
    )

    class Meta:
        ordering = ['-created_at']

    @property
    def total_price(self):
        total_price = 0
        for order_item in self.items.all():
            total_price += order_item.total_price
        return total_price
    
    def __str__(self):
        return f"Заказ номер {self.id} для {self.user}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    @property
    def total_price(self):
        total_price = self.quantity * self.item.price
        return total_price

    def __str__(self):
        return f"{self.quantity} x {self.item.title} in Order {self.order.id}"