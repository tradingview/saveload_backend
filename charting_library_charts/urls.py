from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^1\.0/', include('api.v10.urls')),
    url(r'^1\.1/', include('api.v11.urls')),
)
