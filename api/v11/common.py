from django.http import HttpResponse
import json


def response(content):
	result = HttpResponse(content)
	result["Access-Control-Allow-Origin"] = "*"
	result["Access-Control-Allow-Methods"] = "GET, POST, DELETE, OPTIONS"
	return result


def error(text):
	return response(json.dumps({'status': 'error','message': text}))


def respondToOptionsRequest(requestHeaders):
	result = response(json.dumps({'status': "ok"}))
	result["Access-Control-Allow-Headers"] = requestHeaders["HTTP_ACCESS_CONTROL_REQUEST_HEADERS"]
	return result


def parseRequest(request):
	clientId = request.GET.get('client', '')
	userId = request.GET.get('user', '')

	err = None
	response = None

	if (clientId == ''):
		err = error('Wrong client id')
	elif (userId == ''):
		err = error('Wrong user id')
	elif request.method == 'OPTIONS':
		response = respondToOptionsRequest(request.META)

	return {
		"error": err,
		"response": response,
		"clientId": clientId,
		"userId": userId
	}
