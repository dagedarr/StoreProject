from django.urls import path
from .views import item_details, store

urlpatterns = [
    path('', store, name='home'),
    path('<int:item_id>', item_details, name='item_details')
]
