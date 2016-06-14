from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

admin.autodiscover()
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('core.urls',  namespace='core')),
    url(r'^', include('works.urls', namespace='works')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + staticfiles_urlpatterns()
