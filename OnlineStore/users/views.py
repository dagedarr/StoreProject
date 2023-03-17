from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.shortcuts import render

from checkout.models import Order
from .forms import CreationForm


@login_required
def user_orders(request):
    orders = Order.objects.filter(user=request.user)
    context = {
        'orders': orders,
    }
    return render(request, 'users/user_orders.html', context)


@login_required
def profile(request):
    return render(request, 'users/profile.html')


class SignUp(CreateView):
    form_class = CreationForm
    success_url = reverse_lazy('store:home')
    template_name = 'users/signup.html'
