def wsgi_application(environ, start_response):
    query = environ['QUERY_STRING']
    query_dict = query.split('&')
    res_body = '\n'.join(query_dict)
    res_body_bites = res_body.encode()

    status = '200 OK'
    headers = [
            ('Content-type', 'text/plain')
    ]
    
    start_response(status, headers)
    return iter([res_body_bites])
