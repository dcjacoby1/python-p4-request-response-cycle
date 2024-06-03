#!/usr/bin/env python3

import os

from flask import Flask, request, current_app, g, make_response

app = Flask(__name__)

#lets all our views know where our application files are located
#app.before_request runs before each request
#g.path is equal to /Users/a/Development/code/phase-4/python-p4-request-response-cycle/server
@app.before_request
def app_path():
    g.path = os.path.abspath(os.getcwd())

@app.route('/')
def index():
    #host in this case is 127.0.0.1:5555
    host = request.headers.get('Host')
    #current_app.name in this case is app bc of the line app = Flask(__name__)
    appname = current_app.name
    response_body = f'''
        <h1>The host for this page is {host}</h1>
        <h2>The name of this application is {appname}</h2>
        <h3>The path of this application on the user's device is {g.path}</h3>
    '''

    #good status code - means successful
    status_code = 200
    #object form for headers
    #example header: 'Content-Type': 'text/html'
    headers = {}

    #make_response is a built in function in flask for http response
    # can accept 3 args but not all are needed
    return make_response(response_body, status_code, headers)

#replaces the need for FLASK_APP=app.py and export FLASK_RUN_PORT=5555 followed by flask run
#now I can just do python app.py 
if __name__ == '__main__':
    app.run(port=5555, debug=True)
