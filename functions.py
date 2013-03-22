import smtplib
import pymongo
#import sendgrid
import random

connection = pymongo.Connection('mongodb://santa:balls@linus.mongohq.com:10040/secret_santa')
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
	if collection.find({"name": name}).count() == 0 and collection.find({"email": email}).count() == 0:
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
	#Because the collection is sorted in a random order, I will take each person,
	#and pair them up with the next person in the collection. The last person will
	#be paired with the first. This way, there will be no repeats.

	#Variables I am using for control flow. There is probably a more elegant way to do this.
	first_flag = 1
	previous = ""
	first_user = ""

	for user in collection.find().sort("random number", 1):
		if first_flag == 1:
			first_flag = 0
			first_user = user
			previous = user
		else:
			send_email(previous["email"], previous["name"], user["name"], user["about"], user["email"])
			print "Giver: " + previous["name"] + " taker: " + user["name"]
			previous = user

	send_email(previous["email"], previous["name"], first_user["name"], first_user["about"], first_user["email"])
	print "Giver: " + previous["name"] + " taker: " + first_user["name"]

def send_email(recipient, name_of_recipient, name, about, email):
	#Sends an email
	from_user = 'USACS Secret Santa'
	msg = 'Dear ' + name_of_recipient + ',\n\n' + 'Your assignment for the USACS Secret Santa event is ' + name + '. Here is what ' + name + ' had to say: \n\n' + about + '\n\n ' + name + '\'s email address in case you need it: ' + email
	subject = "Subject: %s\r\n"%("USACS Secret Santa results!")

	username = 'sagnew92'
	password = 'ffvii2981'

	# The actual mail send
	server = smtplib.SMTP('smtp.gmail.com:587')
	server.starttls()
	server.login(username,password)
	server.sendmail(from_user, recipient, subject+msg)
	server.quit()
