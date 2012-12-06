import pymongo
import sendgrid
import random

connection = pymongo.Connection()
db = connection.secret_santa
collection = db.gift_givers

#This stores the people who tried to get multiple gifts so we can laugh at them later.
naughty_list = db.naughty_list

class MultipleUserException(Exception):
#Exception thrown when a user tries to enter him/her self into the database twice
#This means that the user is totally trying to gip USACS into giving them extra presents.
	def __init__(self, message):
		self.message = message
	
def insert_into_db(name, about, email):
	#Inserts a user's information into the collection
	post = {"name": name,
				"about": about,
				"email": email,
				"random number": random_number()
				}
	#Only insert if the user is not already in the collection
	if collection.find({"name": name, "email": email}).count() == 0:
		collection.insert(post)
	else:
		naughty_list.insert(post)
		raise MultipleUserException("You have been added to the naughty list!") 

def random_number():
	#generates a random integer
	random.seed()
	return random.randint(0, 99999)

def pair_users():
	#Pairs users randomly with each other
	
	users = []
	paired = ""
	#This is retarded, and my brain is not working
	#Note to self out of laziness:
	#Because the collection is sorted in a random order, I will take each person,
	#and pair them up with the next person in the collection. The last person will 
	#be paired with the first. This way, there will be no repeats. 
	for item in collection.find().sort("random number", 1):
		users.append(item)
		

def send_email(recipient, name, about, email):
	#Do this later with sendgrid
	return

for user in collection.find():
	print user
