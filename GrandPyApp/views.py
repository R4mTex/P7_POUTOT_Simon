from flask import Flask, render_template, request
from GrandPyApp.scripts.python.parser import Parser
from GrandPyApp.scripts.python.geocoder_api import Geocoder
from GrandPyApp.scripts.python.wikipedia import Wikipedia
from GrandPyApp.scripts.python.grand_py_ansers import Grand_py_ansers


app = Flask(__name__, instance_relative_config=True)
app.config.from_pyfile('config.py')

# app = Flask(__name__)
# app.config.from_object('config')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/index_question', methods=['POST'])
def index_question():
    question = request.form.get('question', False)
    question_parsed = Parser.script_for_parse(question)

    wikipedia_summary = Wikipedia.wiki_page(question_parsed)

    geocoder_request = Geocoder(question_parsed).geocoder_api_request()
    query_location = Geocoder(geocoder_request).get_information_from_the_request()

    if query_location['status'] == 'OK':

        long_name = query_location['long_name']
        query_lat = query_location['lat']
        query_lng = query_location['lng']
        place_id = query_location['place_id']
        random_positive_anser = Grand_py_ansers.random_positive_anser()

        data = {
            'status': query_location['status'],
            'long_name': long_name,
            'lat': query_lat,
            'lng': query_lng,
            'place_id': place_id,
            'wikipedia_summary': wikipedia_summary,
            'random_positive_anser': random_positive_anser,
            }
        return data
    elif query_location['status'] != 'OK':

        random_negative_anser = Grand_py_ansers.random_negative_anser()

        data = {
            'status': query_location['status'],
            'random_negative_anser': random_negative_anser,
            }
        return data
