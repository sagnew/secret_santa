from flask import Flask
from flask import render_template
from flask import request
from functions import *

app = Flask(__name__)

@app.route('/')
def main_page():
	return render_template('main.html')

if __name__ == '__main__':
	app.run(debug=False)
