from django.conf.urls.static import static
from django.contrib import admin
from django.template.defaulttags import url
from django.urls import path
from safepass import settings
from safepass.views import index
from django.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('user.urls')),
    path('genrator/', include('generator.urls')),
    path('contact/', include('contact.urls')),
    path('', index, name='index'),
    url("", include('pwa.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
