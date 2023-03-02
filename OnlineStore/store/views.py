from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, render
from .models import Item, ItemTag



def store(request):
    items = Item.objects.all()
    paginator = Paginator(items, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {'page_obj': page_obj,
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
    tag = get_object_or_404(ItemTag, slug=slug)
    items= Item.objects.filter(tags__in=[tag])
    context = {
        'tag': tag,
        'items': items
        }
    return render(request, 'store/tag_details.html', context)

def tag_list(request):
    tags =ItemTag.objects.all()
    context = {'tags': tags,
    }
    return render(request, 'store/tag_list.html', context)