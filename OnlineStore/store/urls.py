from django.urls import path

from .views import item_details, store, tag_details, tag_list

app_name = 'store'


urlpatterns = [
    path('', store, name='home'),
    path('categories/', tag_list, name='tag_list'),
    path('category-details/<slug:slug>/', tag_details, name='tag_details'),
    path('<slug:item_slug>/', item_details, name='item_details'),
]
