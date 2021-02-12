from django.conf.urls import include, url
from django.contrib import admin


urlpatterns = [
    url(r'^', include('simplemooc_backend.core.urls', namespace='core')),
    url(r'^admin/', include(admin.site.urls)),
]

