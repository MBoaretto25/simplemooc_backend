from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    url(r'^', include('simplemooc_backend.core.urls', namespace='core')),
    url(r'^courses/', include('simplemooc_backend.courses.urls', namespace='courses')),
    url(r'^admin/', include(admin.site.urls)),
]

"""
 Isso server apenas para ambiente de desenvolvimento aonde é necessário apontar o local dos arquivos estáticos.
 Pois o django em modo debug não server os arquivos. 
 Em servidores de produção é utilizado um servidor a parte para os arquivos estáticos.
"""
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
