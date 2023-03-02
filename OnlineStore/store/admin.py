from django.contrib import admin
from .models import Item, ItemTag

class ItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'price', 'old_price', 'is_available', 'tag_list')

    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related('tags')

    def tag_list(self, obj):
        return u", ".join(o.name for o in obj.tags.all())
    

class ItemTagAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'description', 'item_list')

    def item_list(self, obj):
        return [Item.objects.get(pk=o.get('object_id')) for o in obj.items.all().values()]
    
 # 'id', 'image', 'items', 'name', 'objects', 'pk',

admin.site.register(Item, ItemAdmin)
admin.site.register(ItemTag, ItemTagAdmin)