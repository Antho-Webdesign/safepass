from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from safepass import settings
from safepass.views import index


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('user.urls')),
    path('', index, name='index'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
