from django.urls import path
from .views import store

urlpatterns = [
    path('', store),
]
