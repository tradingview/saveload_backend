from django.conf.urls import patterns, url
import charts
import studyTemplates
from django.views.decorators.csrf import csrf_exempt


urlpatterns = patterns('',
	url(r'^charts$', csrf_exempt(charts.processRequest)),
)

urlpatterns = patterns('',
	url(r'^study_templates$', csrf_exempt(studyTemplates.processRequest)),
)
