from django.urls import include, re_path as url

urlpatterns = [
    url(r'^1\.0/', include('api.v10.urls')),
    url(r'^1\.1/', include('api.v11.urls')),
    url(r'', include('django_prometheus.urls')),
]
