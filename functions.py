import pymongo
import sendgrid

connection = pymongo.Connection()
db = connection.secret_santa
collection = db.gift_givers

def insert_into_db(name, about, email):
	#Inserts a user's information into the collection

	#Only insert if the user is not already in the collection
	if collection.find({"name": name, "email": email}).count() == 0:
		post = {"name": name,
				"about": about,
				"email": email
				}
		collection.insert(post)

def send_email(recipient, name, about, email):
	#Do this later with sendgrid
	return

