from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def home():
    if request.method == 'POST':
        print(request.get_json())
        return request.get_json()['name']
    return 'Hola mundo'

if '__main__' == __name__:
    app.run(debug = True)