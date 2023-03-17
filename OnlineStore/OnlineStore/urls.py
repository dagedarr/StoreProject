from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cart/', include('cart.urls')),
    path('about/', include('about.urls')),
    path('checkout/', include('checkout.urls')),
    path('users/', include('users.urls')),
    path('', include('store.urls')),
    path('', include('django.contrib.auth.urls'))
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
