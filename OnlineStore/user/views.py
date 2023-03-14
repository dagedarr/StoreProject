from django.shortcuts import render

from checkout.models import Order

def profile(request, username):
    orders = Order.objects.filter(user=request.user)
    context = {
        'orders': orders,
    }
    return render(request, 'user/profile.html', context)
