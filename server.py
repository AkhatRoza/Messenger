from flask import Flask,request,abort
from datetime import datetime
import time

app = Flask(__name__)
messages = [
    {'name':'Jack','time': time.time(),'text':'123'},
    {'name':'Jack','time': time.time(),'text':'1234'}
]

users = {
    'Jack':'12345'
}
@app.route('/')
def hello_world_view():
    return 'Hello, World! <a href="/status">Status,</a>'

@app.route('/status')
def status_view():
    return {
        'status': True,
        'name': 'ABC',
        'time1': datetime.now().strftime('%Y/%m/%d %H-%M-%S'),
        'time2': datetime.now().isoformat(),
        'time3': time.time(),
        'time4': time.asctime()
    }

@app.route('/send', methods = ['POST'])
def send_view():
    name = request.json.get('name')
    password = request.json.get('password')
    text = request.json.get('text')

    for token in (name,password,text):
        if not isinstance(token,str) or not len(token) or len(token) > 1024:
            abort(400)


    if name in users:
        if users[name] !=password:
            abort(401)
    else:
        users[name]=password

    messages.append({'name':name,'text': text,'time': time.time()})




    return {'ok':True}


def filter_dicts(elements,key,min_value):
    new_elements =[]

    for element in elements:
        if element[key] > min_value:
            new_elements.append(element)

    return new_elements


@app.route('/messages')
def messages_view():
    after = float(request.args['after'])
    filtered_messages = filter_dicts(messages,key = 'time',min_value=after)
    return {'messages':filtered_messages}

app.run()