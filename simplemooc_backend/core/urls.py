from django.conf.urls import url, patterns


urlpatterns = patterns('simplemooc_backend.core.views',
                       url(r'^$', 'home', name='home'),
                       url(r'^core/$', 'contact', name='contact'),
                       )

