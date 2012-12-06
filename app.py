from flask import Flask
from flask import render_template
from flask import request
from functions import *

app = Flask(__name__)

@app.route('/')
def main_page():
	return render_template('main.html')

@app.route('/', methods=['POST'])
def post_data():
	name = request.form["_name"]
	about = request.form["_about"]
	email = request.form["_email"]
	insert_into_db(name, about, email)

if __name__ == '__main__':
	app.run(host='0.0.0.0')


