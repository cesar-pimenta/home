from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from django.contrib.sitemaps.views import sitemap
from filebrowser.sites import site
from core.sitemaps import PostSitemap

sitemaps = {
    'posts': PostSitemap,
}

urlpatterns = [
    path('admin/filebrowser/', site.urls),
    path('grappelli/', include('grappelli.urls')),
    path('admin/', admin.site.urls),
    path('', include('landing_page.urls', namespace='landing_page')),
    path('account/', include('account.urls', namespace='account')),
    path('blog/', include('core.urls', namespace='core')),
    path('images/', include('images.urls', namespace='images')),
    path('schedule/', include('schedule.urls', namespace='schedule')),
    path('mission/', include('mission.urls', namespace='mission')),
    path('store/', include('store.urls', namespace='store')),
    path('cart/', include('cart.urls', namespace='cart')),
    path('orders/', include('orders.urls', namespace='orders')),
    path('enrollment/', include('enrollment.urls', namespace='enrollment')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps},
         name='django.contrib.sitemaps.views.sitemap'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)