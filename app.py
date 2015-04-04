
import os

import flask

app = flask.Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'this_should_be_configured')


@app.route('/')
def home():
    return "OK"


@app.errorhandler(404)
def page_not_found(error):
    return "Not found", 404


if __name__ == '__main__':
    app.run(debug=True)
