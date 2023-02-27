from django.urls import path
from .views import item_details, store

urlpatterns = [
    path('', store),
    path('<int:item_id>', item_details)
]
