from django.http import HttpResponse
from model import models
import json
from datetime import datetime
import time
from . import common


def processRequest(request):
	parsedRequest = common.parseRequest(request)

	if !(parsedRequest.error is None):
		return parsedRequest.error

	clientId = parsedRequest.clientId
	userId = parsedRequest.userId
	templateId = request.GET.get('template', '')


	if request.method == 'GET':
		if templateId == '':
			return getAllTemplatesList(clientId, userId)
		else:
			return getTemplate(clientId, userId, templateId)

	elif request.method == 'DELETE':
		if templateId == '':
			return common.error('Wrong template id')
		else:
			return removeTemplate(clientId, userId, templateId)

	elif request.method == 'POST':
		chartName = request.POST.get('name')
		symbol = request.POST.get('symbol')
		resoluion = request.POST.get('resolution')
		content = request.POST.get('content')
		if templateId == '':
			return saveChart(clientId, userId, chartName, symbol, resoluion, content)
		else:
			return rewriteChart(clientId, userId, templateId, chartName, symbol, resoluion, content)

	else:
		return common.error('Wrong request')

#-----------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------


def getAllTemplatesList(clientId, userId):
	items = models.StudyTemplate.objects.filter(ownerSource = clientId, ownerId = userId)
	result = map(lambda x : {'name': x.name} , items)
	return common.response(json.dumps({'status': "ok", 'data': list(result)}))


def getTemplate(clientId, userId, name):
	try:
		item = models.StudyTemplate.objects.get(ownerSource = clientId, ownerId = userId, name = name)
		result = json.dumps({'status': 'ok', 'data': { 'name': item.name, 'content': item.content}})
		return common.response(result)
	except:
		return common.error('StudyTemplate not found')


def removeTemplate(clientId, userId, name):
	try:
		item = models.StudyTemplate.objects.get(ownerSource = clientId, ownerId = userId, name = name)
		item.delete()
		return common.response(json.dumps({'status': 'ok'}))
	except:
		return common.error('StudyTemplate not found')


def createTemplate(clientId, userId, name, content):
	newItem = models.StudyTemplate(
		ownerSource = clientId,
		ownerId = userId,
		name = name,
		content = content
	)

	newItem.save()
	return common.response(json.dumps({'status': 'ok'}))


def rewriteTemplate(clientId, userId, name, content):
	try:
		chart = models.StudyTemplate.objects.get(ownerSource = clientId, ownerId = userId, id = chartId)
		chart.lastModified = datetime.utcnow()
		chart.content = content
		chart.name = chartName
		chart.symbol = symbol
		chart.resolution = resolution

		chart.save()
		return common.response(json.dumps({'status': 'ok'}))
	except:
		return common.error('StudyTemplate not found')
