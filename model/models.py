from django.db import models
from django_prometheus.models import ExportModelOperationsMixin
from jsonfield import JSONField


class Chart(ExportModelOperationsMixin('charts'), models.Model):
	id = models.BigAutoField(primary_key=True)
	ownerSource = models.CharField(max_length=200, db_index=True)
	ownerId = models.CharField(max_length=200, db_index=True)
	name = models.CharField(max_length=200)
	symbol = models.CharField(max_length=50)
	resolution = models.CharField(max_length=10)
	lastModified = models.DateTimeField()
	content = JSONField()

	def __str__(self):
		return self.ownerSource + ":" + self.ownerId

	def setContent(self, _content):
		self.content = _content


class StudyTemplate(ExportModelOperationsMixin('study_template'), models.Model):
	id = models.BigAutoField(primary_key=True)
	ownerSource = models.CharField(max_length=200, db_index=True)
	ownerId = models.CharField(max_length=200, db_index=True)
	name = models.CharField(max_length=200)
	content = JSONField()

	def __str__(self):
		return self.ownerSource + ":" + self.ownerId

	def setContent(self, _content):
		self.content = _content


class DrawingTemplate(ExportModelOperationsMixin('drawing_template'), models.Model):
	id = models.BigAutoField(primary_key=True)
	ownerSource = models.CharField(max_length=200, db_index=True)
	ownerId = models.CharField(max_length=200, db_index=True)
	name = models.CharField(max_length=200)
	tool = models.CharField(max_length=200)
	content = JSONField()

	def __str__(self):
		return self.ownerSource + ":" + self.ownerId

	def setContent(self, _content):
		self.content = _content
