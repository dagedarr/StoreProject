from django.shortcuts import get_object_or_404, render
from .models import Item

def store(request):
    items = Item.objects.all()
    context = {'items': items}
    return render(request, 'store/main_page.html', context)

def item_details(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    context = {'item': item}
    return render(request, 'store/item_details.html', context)    
