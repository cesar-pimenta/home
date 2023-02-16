from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('landing_page.urls', namespace='landing_page')),
    path('blog/', include('core.urls', namespace='core')),
]
