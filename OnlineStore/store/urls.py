from django.urls import path, re_path
from .views import item_details, store, tag_details

urlpatterns = [
    path('', store, name='home'),
    path('<int:item_id>/', item_details, name='item_details'),
    path('tag-details/<slug:slug>/', tag_details, name='tag_details')
]
