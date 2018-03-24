#import the important libraries
import os, time
import random
import sys
#now lets create thes words for incoming
nameIn = ['what is your name', 'whats your name', 'what is your name?', 'whats your name?']
greetIn = ['hello', 'hi', 'hi there', 'hello there']
birth = ['what is your date of birth', 'what is your date ofbirth?', 'what is yourDOB', 'what is yourDOB?']
botmaster = ['who is your botmaster', 'who is your botmaster?', 'who is your father', 'who is your mother']
#will also need to create outgoing
greetOut = ['hi there','hello','hi my name is Ralfy','hello there']
nameout = ['Iam called Ralfy', 'My name is Ralfy', 'Imcalled Ralfy']
while True:
	H = raw_input('You:').strip()
	HLower = H.lower()

	if H == '':
		print 'Bot: Thanks meeting you'
		sys.exit()
		break
	elif HLower in nameIn:
		print 'Bot:'+(random.choice(nameout))
	elif HLower in greetIn:
		print 'Bot:' +(random.choice(greetOut))
	elif HLower in botmaster:
		print 'Bot: My botmaster is Alfy'
	elif HLower in birth:
		print 'Bot: I was activated in the 25th of February 2017'
	else:
		print 'Bot: Your question sounds good but can you ask another question please?'

