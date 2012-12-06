import pymongo
import sendgrid
import random

connection = pymongo.Connection()
db = connection.secret_santa
collection = db.gift_givers

def insert_into_db(name, about, email):
	#Inserts a user's information into the collection

	#Only insert if the user is not already in the collection
	if collection.find({"name": name, "email": email}).count() == 0:
		post = {"name": name,
				"about": about,
				"email": email,
				"random number": random_number()
				}
		collection.insert(post)

def random_number():
	#generates a random integer
	random.seed()
	return random.randint(0, 99999)

def pair_users():
	#Pairs users randomly with each other

	users = []
	#This is retarded, and my brain is not working
	for item in collection.find().sort("random number", 1):
		users.append(item)
	print random.choice(users)

def send_email(recipient, name, about, email):
	#Do this later with sendgrid
	return

