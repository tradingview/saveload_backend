from django.urls import include, re_path

urlpatterns = [
    re_path(r'^1\.0/', include('api.v10.urls')),
    re_path(r'^1\.1/', include('api.v11.urls')),
    re_path(r'', include('django_prometheus.urls')),
]
