import pymongo

def insert_into_db(name, about, email):
	#Inserts a user's information into the collection
	post = {"name": name,
			"about": about,
			"email": email
			}
	
	if post not in collections:
		collections.insert(post)
