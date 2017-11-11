
from cgi import parse_qs, escape

def get_post(environ, start_response):
	lines = []
	if environ['REQUEST_METHOD']=='GET':
		key = 'REQUEST_METHOD'
		value = environ['REQUEST_METHOD']
		lines.append("%s: %r" % (key, value))	
		key = 'PARAMETERS'
		value = environ['QUERY_STRING']
		lines.append("%s: %r" % (key, value))
		start_response("200 OK", [("Content-Type", "text/plain")])
		return ["\n".join(lines)]
	else:
		try:
			request_body_size = int(environ.get('CONTENT_LENGTH', 0))
		except (ValueError):
			request_body_size = 0
		request_body = environ['wsgi.input'].read(request_body_size)
		d = parse_qs(request_body)
		name = d.get('name', [''])[0]
		status = '200 OK'
		response_headers = [('Content-type', 'text/plain')]
		start_response(status, response_headers)
		return ([name.encode()])
