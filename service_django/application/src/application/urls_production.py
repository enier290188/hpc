from . import views
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static

urlpatterns = [
    url(regex=r'^$', view=views.___view___index___, name='application'),
    url(r'^website/', include('src.application.website.urls', namespace='application___website')),
    url(r'^hpc/', include('src.application.hpc.urls', namespace='application___hpc')),
    url(r'^bigdata/', include('src.application.bigdata.urls', namespace='application___bigdata')),
    url(r'^administration/', include('src.application.administration.urls', namespace='application___administration')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
