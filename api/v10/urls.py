from django.urls import re_path
from . import views
from django.views.decorators.csrf import csrf_exempt

#GET 	charts?userid=0&clientid=1
#GET 	charts?userid=0&clientid=1&chartid=2
#DELETE charts?userid=0&clientid=1&chartid=2
#POST 	charts?userid=0&clientid=1&chartid=2
#POST 	charts?userid=0&clientid=1

urlpatterns = [
	re_path(r'^charts$', csrf_exempt(views.doTheMagic)),
]
