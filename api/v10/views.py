from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from charts import models
import json
from datetime import datetime
import time

def error(text):
	return HttpResponse(json.dumps({'status': 'error','message': text}))

@csrf_exempt
def doTheMagic(request):
	clientId = request.GET.get('client', '')

	if (clientId == ''):
		return error('Wrong client id')

	userId = request.GET.get('user', '')

	if (userId == ''):
		return error('Wrong user id')

	chartId = request.GET.get('chart', '')

	if request.method == 'GET':
		if chartId == '':
			return getAllUserCharts(clientId, userId)
		else:
			return getChartContent(clientId, userId, chartId)

	elif request.method == 'DELETE':
		if chartId == '':
			return error('Wrong chart id')
		else:
			return removeChart(clientId, userId, chartId)

	elif request.method == 'POST':
		chartName = request.POST.get('name')
		content = request.POST.get('content')
		if chartId == '':
			return saveChart(clientId, userId, chartName, content)
		else:
			return rewriteChart(clientId, userId, chartId, chartName, content)

	else:
		return error('Wrong request')


def response(content):
	result = HttpResponse(content)
	return result


def getAllUserCharts(clientId, userId):
	chartsList = models.Chart.objects.filter(ownerSource = clientId, ownerId = userId)
	result = map(lambda x : {'id': x.id, 'name': x.name, 'timestamp': time.mktime(x.lastModified.timetuple())} , chartsList)
	return response(json.dumps({'status': "ok", 'data': result}))


def getChartContent(clientId, userId, chartId):
	try:
		chart = models.Chart.objects.get(ownerSource = clientId, ownerId = userId, id = chartId)
		result = json.dumps({'status': 'ok', 'id': chart.id, 'name': chart.name, 'timestamp': time.mktime(chart.lastModified.timetuple()), 'content': chart.content})
		return response(result)
	except:
		return error('Chart not found')


def removeChart(clientId, userId, chartId):
	try:
		chart = models.Chart.objects.get(ownerSource = clientId, ownerId = userId, id = chartId)
		chart.delete()
		return response(json.dumps({'status': 'ok'}))
	except:
		return error('Chart not found')


def saveChart(clientId, userId, chartName, content):
	newChart = models.Chart(ownerSource = clientId, ownerId = userId, name = chartName, content = content, lastModified = datetime.utcnow())
	newChart.save()
	return response(json.dumps({'status': 'ok', 'id': newChart.id}))


def rewriteChart(clientId, userId, chartId, chartName, content):
	try:
		chart = models.Chart.objects.get(ownerSource = clientId, ownerId = userId, id = chartId)
		chart.lastModified = datetime.utcnow()
		chart.content = content
		chart.name = chartName

		chart.save()
		return response(json.dumps({'status': 'ok'}))
	except:
		return error('Chart not found')