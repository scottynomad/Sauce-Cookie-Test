from werkzeug.wrappers import Request, Response

def application(environ, start_response):
    request = Request(environ)
    path = request.path[1:].split('/')

    name = 'root'
    count = 2
    if len(path) > 1:
        count = int(path[1])
    if len(path) > 0:
        name = path[0] or 'root'

    html = """
        <html>
            <head><title>Cookie Test</title></head>
            <body>Dropped cookies under name <em>%s</em></body>
        </html>
    """
    response = Response(html % name, mimetype='text/html')
    for n in range(count):
        response.set_cookie('%s%d' % (name, n), 'stuff')
    return response(environ, start_response)


