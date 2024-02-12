from django.urls import re_path
from api.v11 import studyTemplates
from api.v11 import drawingTemplates
from api.v11 import charts
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
	re_path(r'^charts$', csrf_exempt(charts.processRequest)),
	re_path(r'^study_templates$', csrf_exempt(studyTemplates.processRequest)),
	re_path(r'^drawing_templates$', csrf_exempt(drawingTemplates.processRequest)),
]
