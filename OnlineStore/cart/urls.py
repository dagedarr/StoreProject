from django.urls import path
from .views import add_to_cart, cart, remove_from_cart

app_name = 'cart'

urlpatterns = [
    path('', cart, name='cart'),
    path('add/<slug:item_slug>/', add_to_cart, name='add_to_cart'),
    path('remove/<slug:item_slug>/', remove_from_cart, name='remove_from_cart'),
    # path('cart/checkout/', views.checkout, name='checkout'),
]
