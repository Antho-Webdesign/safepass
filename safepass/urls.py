from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from safepass import settings
from safepass.views import index


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('user.urls')),
    path('genrator/', include('generator.urls')),
    path('contact/', include('contact.urls')),
    path('', index, name='index'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
