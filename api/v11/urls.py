from django.conf.urls import patterns, url
from api.v11 import studyTemplates
from api.v11 import charts
from django.views.decorators.csrf import csrf_exempt


urlpatterns = patterns('',
	url(r'^charts$', csrf_exempt(charts.processRequest)),
	url(r'^study_templates$', csrf_exempt(studyTemplates.processRequest)),
)
