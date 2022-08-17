"""
venv\Scripts\Activate.ps1
"""
from flask import Flask, render_template, request, json
from GrandPyApp.script.parser import Parser

app = Flask(__name__)
app.config.from_object('config')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/index_question', methods=['POST'])
def index_question():
    question = request.form['question']
    question_parsed = Parser.script_for_parse(question)
    return json.dumps({'status':'OK','question':question_parsed}, indent=2)
