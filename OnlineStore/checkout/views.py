from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from .forms import OrderCreateForm
from .models import Order, OrderItem, ShippingAddress
from cart.views import Cart


def checkout(request):
    """
    Представление чекаута.
    """
    cart = Cart.objects.get(user=request.user)
    form = OrderCreateForm()
    context = {
        'cart': cart,
        'form': form,
    }

    return render(request, 'checkout/checkout.html', context)


def thank_you(request, order_id):
    """
    Страница благодарности за заказ.
    """
    order = get_object_or_404(Order, id=order_id, user=request.user)
    return render(request, 'checkout/thank_you.html', {'order': order})


def create_order(request):
    """
    Создание экземпляров Order и ShippingAddress
    из формы и редирект в профиль пользователя,
    либо передаем форму обратно.
    """
    cart = get_object_or_404(Cart, user=request.user)

    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            shipping_address = ShippingAddress.objects.create(
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                email=form.cleaned_data['email'],
                phone=form.cleaned_data['phone'],
                address_line_1=form.cleaned_data['address_line_1'],
                address_line_2=form.cleaned_data['address_line_2'],
            )

            order = Order.objects.create(
                payment_method=form.cleaned_data['payment_method'],
                user=request.user,
                shipping_address=shipping_address,
            )

            for cart_item in cart.items.all():
                OrderItem.objects.create(
                    order=order,
                    item=cart_item.item,
                    quantity=cart_item.quantity,
                    price=cart_item.item.price
                )

            cart.clear()
            return redirect('checkout:thank_you', order_id=order.id)
    else:
        form = OrderCreateForm()
    messages.warning(
        request, 'Форма не была корректно обработана, введите данные еще раз')
    context = {'form': form, 'cart': cart}
    return render(request, 'checkout/checkout.html', context)
