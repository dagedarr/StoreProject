from django.http import JsonResponse
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


def delete_cart_item(request, item_slug):
    cart_item = CartItem.objects.get(
        cart=Cart.objects.get(user=request.user),
        item=get_object_or_404(Item, slug=item_slug)
    )
    cart_item.delete()

    return redirect('cart:cart')


def update_cart_item(request):
    if request.method == 'POST':
        cart_item_id = request.POST.get('cart_item_id')
        new_quantity = int(request.POST.get('new_quantity'))
        cart_id = int(request.POST.get('cart_id'))

        cart = Cart.objects.get(pk=cart_id)

        print(111111111111111)

        cart_item = get_object_or_404(CartItem, id=cart_item_id)
        cart_item.quantity = new_quantity
        cart_item.save()
        
        print(f'CART TP = {cart.total_price}')
        return JsonResponse({
            'success': True,
            'cart_item_id': cart_item.id,
            'cart_item_quantity': cart_item.quantity,
            'cart_item_total_price': cart_item.total_price,
            'cart_total_price': cart.total_price
        })
    else:
        return JsonResponse({'success': False, 'error': 'Invalid request method'})
