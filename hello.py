from urllib.parse import parse_qs
from re import sub

def app(environ, start_response):
	status = "200 OK"
	data = b'Hello, world!\n'
	response_headers = [
	('Content-type', 'text/plain'),
	('Content-Length', str(len(data)))
	]
	start_response(status, response_headers)
	print(environ.get('QUERY_STRING'))
	return iter([data])
