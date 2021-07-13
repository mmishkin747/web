

def app(environ, start_response):
	status = "200 OK"
	data = b'Hello, world!\n'
	response_headers = [
	('Content-type', 'text/plain'),
	('Content-Length', str(len(data)))
	]
	body = [bytes(i + '\n', 'ascii') for i in environ['QUERY_STRING'].split('&')]
	start_response(status, response_headers)
	return iter(body)
