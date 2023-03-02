from django.shortcuts import get_object_or_404, render
from .models import Item, ItemTag
from .paginator import paginator


def store(request):
    items = Item.objects.all()
    context = {
        'page_obj': paginator(request, items, 6),
        'range': [*range(1,7)], # For random css styles
    }

    return render(request, 'store/main_page.html', context)

def item_details(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    context = {
        'item': item,
        }
    return render(request, 'store/item_details.html', context)    

def tag_details(request, slug):
    tag = get_object_or_404(ItemTag, slug=slug)
    items= Item.objects.filter(tags__in=[tag])
    context = {
        'tag': tag,
        'page_obj': paginator(request, items, 3),
        }
    return render(request, 'store/tag_details.html', context)

def tag_list(request):
    tags = ItemTag.objects.all()
    context = {
        'page_obj': paginator(request, tags, 6),
    }
    return render(request, 'store/tag_list.html', context)