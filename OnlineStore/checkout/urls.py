from django.urls import path
from .views import checkout

app_name = 'checkout'

urlpatterns = [
    path('', checkout, name='checkout'),
]