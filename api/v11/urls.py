from django.conf.urls import url
from api.v11 import studyTemplates
from api.v11 import drawingTemplates
from api.v11 import charts
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
	url(r'^charts$', csrf_exempt(charts.processRequest)),
	url(r'^study_templates$', csrf_exempt(studyTemplates.processRequest)),
	url(r'^drawing_templates$', csrf_exempt(drawingTemplates.processRequest)),
]
