from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from functions import *
import os

app = Flask(__name__)

@app.route('/')
def main_page():
	return render_template('main.html')

@app.route('/submit', methods=['POST'])
def post_data():
	name = request.form["_name"]
	about = request.form["_about"]
	email = request.form["_email"]
	try:
		insert_into_db(name, about, email)
		return redirect('/success', 301)
	except MultipleUserException:
		return redirect('/naughty', 301)

@app.route('/success')
def sucess_page():
	return render_template('success.html')

@app.route('/naughty')
def naughty_page():
	return render_template('naughty.html')

if __name__ == '__main__':
	port = int(os.environ.get("PORT",5000))
	app.run(host='0.0.0.0', port=port)

