def response(content):
	result = HttpResponse(content)
	result["Access-Control-Allow-Origin"] = "*"
	result["Access-Control-Allow-Methods"] = "GET, POST, DELETE, OPTIONS"
	return result



def error(text):
	return response(json.dumps({'status': 'error','message': text}))


def respondToOptionsRequest(requestHeaders):
	result = common.response(json.dumps({'status': "ok"}))
	result["Access-Control-Allow-Headers"] = requestHeaders["HTTP_ACCESS_CONTROL_REQUEST_HEADERS"]
	return result


def parseRequest(request):
	clientId = request.GET.get('client', '')
	userId = request.GET.get('user', '')

	err = ''

	if (clientId == ''):
		err = error('Wrong client id')

	if (userId == ''):
		err = error('Wrong user id')

	if request.method == 'OPTIONS':
		response = respondToOptionsRequest(request.META)

	return dict(error=err, response=response, clientId=clientId, iserId=userId)
