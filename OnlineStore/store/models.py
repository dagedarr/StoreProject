from django.db import models
from taggit.managers import TaggableManager

class Item(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
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
        upload_to='posts/',
        blank=True
    )
    tags = TaggableManager()

    def __str__(self):
        return self.title


    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


