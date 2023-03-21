from django.urls import path

from .views import checkout, create_order, thank_you

app_name = 'checkout'

urlpatterns = [
    path('', checkout, name='checkout'),
    path('create-order/', create_order, name='create_order'),
    path('thank-you/<int:order_id>/', thank_you, name='thank_you'),
]
