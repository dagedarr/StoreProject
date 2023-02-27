from django.shortcuts import render
from .models import Item

def store(request):
    items = Item.objects.all()
    context = {'items': items}
    return render(request, 'store/main_page.html', context)
