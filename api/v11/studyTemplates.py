from django.http import HttpResponse
import json
import time
from datetime import datetime

from model import models
from api.v11 import common


def processRequest(request):
	parsedRequest = common.parseRequest(request)

	if parsedRequest['error'] is not None:
		return parsedRequest['error']

	if parsedRequest['response'] is not None:
		return parsedRequest['response']

	clientId = parsedRequest["clientId"]
	userId = parsedRequest['userId']
	templateName = request.GET.get('template', '')


	if request.method == 'GET':
		if templateName == '':
			return getAllTemplatesList(clientId, userId)
		else:
			return getTemplate(clientId, userId, templateName)

	elif request.method == 'DELETE':
		if templateName == '':
			return common.error('Wrong template id')
		else:
			return removeTemplate(clientId, userId, templateName)

	elif request.method == 'POST':
		templateName = request.POST.get('name')
		content = request.POST.get('content')
		return createOrUpdateTemplate(clientId, userId, templateName, content)

	else:
		return common.error('Wrong request')


#-----------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------


def getAllTemplatesList(clientId, userId):
	items = models.StudyTemplate.objects.defer('content').filter(ownerSource = clientId, ownerId = userId)
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


def createOrUpdateTemplate(clientId, userId, name, content):
	newItem, created = models.StudyTemplate.objects.get_or_create(ownerSource=clientId, ownerId=userId, name=name)

	newItem.content = content
	newItem.save()

	return common.response(json.dumps({'status': 'ok'}))
