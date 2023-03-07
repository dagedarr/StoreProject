from django.db import models
from django.utils.translation import gettext_lazy as _
from taggit.managers import TaggableManager
from taggit.models import TagBase, GenericTaggedItemBase


class ItemTag(TagBase):
    image = models.ImageField(
        'Картинка тега',
        upload_to='posts/',
        blank=True
    )
    description = models.TextField(blank=True)

    class Meta:
        verbose_name = _("Tag")
        verbose_name_plural = _("Tags")


class TaggedItem(GenericTaggedItemBase):
    tag = models.ForeignKey(
        ItemTag,
        on_delete=models.CASCADE,
        related_name="items",
    )


class Item(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    slug = models.CharField(
        max_length=50,
        blank=True,
        null=True
    )
    pub_date = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        verbose_name='Новая цена'
    )
    old_price = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        verbose_name='Старая цена',
        blank=True,
        null=True
    )
    image = models.ImageField(
        'Картинка',
        upload_to='items/',
        blank=True
    )
    is_available = models.BooleanField(default=True)
    tags = TaggableManager(through=TaggedItem, related_name="tagged_items")

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-price']
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
