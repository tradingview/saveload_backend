from django.conf.urls import patterns, url
from . import views

#GET 	charts?userid=0&clientid=1
#GET 	charts?userid=0&clientid=1&chartid=2
#DELETE charts?userid=0&clientid=1&chartid=2
#POST 	charts?userid=0&clientid=1&chartid=2
#POST 	charts?userid=0&clientid=1

urlpatterns = patterns('',
	url(r'^charts$', views.doTheMagic),
)
