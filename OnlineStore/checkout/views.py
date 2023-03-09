from django.shortcuts import render


def checkout(request):
    """
    Представление чекаута.
    """

    context = {
    }

    return render(request, 'checkout/checkout.html', context)