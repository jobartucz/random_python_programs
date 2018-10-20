from bottle import route, run, template

@route('/hello/<name>')
def index(name):
    return template('<h1>hi</h1><b>Hello {{name}}</b>!', name=name)

run(host='localhost', port=8080)