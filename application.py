from flask import Flask
application = Flask(__name__) # application is a new instance of Flask

@application.route('/') # create a simple endpoint - default web page
def hello_world():
    return 'Hello there good sir.'
