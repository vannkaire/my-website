from bottle import run,route,template
from datetime import datetime
import requests

@route('/')
def index():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S:%A")
    name = 'David'
    response = requests.get(f'https://api.agify.io/?name={name}')
    response = response.json()
    age = response['age']   
    return template('homepage', time=current_time, name = name, age=age)


#main routine
run(reloader=True)