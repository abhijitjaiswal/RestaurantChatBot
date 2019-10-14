from flask import Flask, Response, render_template, request
from rasa_nlu.model import Interpreter
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

interpertor = Interpreter.load('./models/nlu/default/foodienlu')

@app.route('/nlu_parsing', methods=['POST'])
def transform():
    if request.headers['Content-Type'] == 'application/json':
        query = request.json.get('utterance')
        results = interpertor.parse(query)
        js = json.dumps(results)
        resp = Response(js, status=200, mimetype='application/json')
        return resp

if __name__ == '__main__':
    app.run(debug=True)
