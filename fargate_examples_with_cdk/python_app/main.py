# https://medium.com/@khuva_harkishan/how-to-create-a-web-application-without-any-framework-in-python-fc951f7b9c66
import wsgiref.simple_server


def application(environ, start_response):
    # response
    status = '200 OK'
    response = b"OMG! I'm in Fargate!"
    headers = [('Content-type', 'text/html')]
    start_response(status, headers)

    return [response]


def run():
    httpd = wsgiref.simple_server.make_server('', 8000, application)
    print('Serving on port 8000...')
    httpd.serve_forever()


if __name__ == '__main__':
    run()
