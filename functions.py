import pymongo
import sendgrid

connection = pymongo.Connection()
db = connection.secret_santa
collection = db.gift_givers

def insert_into_db(name, about, email):
	#Inserts a user's information into the collection

	if name not in collection.find("{name: {$in: [name] } }"):
		collection.insert(post)
	else:
		post = {"name": name,
				"about": about,
				"email": email
				}

collection.insert({"name": "ass",
				"about": "ficl",
				"email": "shit"
				})
collection.insert({"name": "hello",
				"about": "ficl",
				"email": "shit"
				})
insert_into_db("ass", "fuck", "shit")
