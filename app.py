from flask import Flask
from flask import render_template
from flask import request
from functions import *

app = Flask(__name__)

class View(flask.views.MethodView):
	def get(self):
		return flask.render_template("templates/main.html")

	def post(self):
		return "Fuck you!"

@app.route('/')
def main_page():
	return render_template('main.html')

if __name__ == '__main__':
	app.run(debug=False)


