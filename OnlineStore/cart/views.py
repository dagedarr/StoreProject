from django.shortcuts import render, redirect, get_object_or_404

from store.models import Item
from .models import Cart, CartItem


def cart(request):
    cart = Cart.objects.filter(user=request.user).first()

    #  cart = Cart.objects.get(user=request.user) (проверить когда у меня будет 2+ корзины, какая будет использована)
    if not cart:
        cart = Cart.objects.create(user=request.user)

    context = {
        'cart_items': CartItem.objects.filter(cart=cart),
        'cart': cart
    }

    return render(request, 'cart/cart.html', context)


def add_to_cart(request, item_slug):
    item = get_object_or_404(Item, slug=item_slug)
    cart, _ = Cart.objects.get_or_create(user=request.user)

    cart_item, created = CartItem.objects.get_or_create(
        cart=cart,
        item=item
    )
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('cart:cart')


def remove_from_cart(request, item_id):
    cart_item = CartItem.objects.get(
        cart=Cart.objects.get(user=request.user),
        item=get_object_or_404(Item, id=item_id)
    )

    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()

    return redirect('store:cart')
