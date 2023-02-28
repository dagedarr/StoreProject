from django.shortcuts import get_object_or_404, render
from .models import Item
from taggit.models import Tag


def store(request):
    items = Item.objects.all()
    context = {'items': items,
               'range': [*range(1,7)],
    }
    return render(request, 'store/main_page.html', context)

def item_details(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    context = {
        'item': item,
        }
    return render(request, 'store/item_details.html', context)    

def tag_details(request, slug):
    tag = get_object_or_404(Tag, slug=slug)
    items= Item.objects.filter(tags__in=[tag])
    context = {
        'tag': tag,
        'items': items
        }
    return render(request, 'store/tag_details.html', context) 