from django.conf.urls import include, url

urlpatterns = [
    url(r'^1\.0/', include('api.v10.urls')),
    url(r'^1\.1/', include('api.v11.urls')),
]
