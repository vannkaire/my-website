'''
My First website with bottle.py
'''
import pytz
from bottle import run,route,template
from datetime import datetime
import requests

@route('/homepage')
def index():
    return template('homepage')



#main routine
run(reloader=True)