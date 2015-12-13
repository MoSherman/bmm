""" This python script pulls data from the bmm MySQL database.
    It's purpose is to allow a user to pull information from the database.
    
    This script is a part of the British Museum Map Project aka bmm. For more on the project see:
    https://github.com/MoSherman/bmm
    
    This is version 1.0 started on Sun Dec 13 18:43:00 GMT 2015
"""

import csv                  # Import csv module
import MySQLdb              # Import MySQLdb module
import os                   # Import os


path  = os.path.expanduser('~/Projects/bmm_private/bmm_login.txt') # Specifying path to login details
login = csv.reader(file(path)) # Creating a list of the login details                                       

# Assign login details to connection variables
for i in login:
    host    = i[0]
    user    = i[1]
    passwd  = i[2]
    db      = i[3]

# Connect to test database
conn    = MySQLdb.connect(host=host, 
                       user=user, 
                       passwd=passwd, 
                       db=db) 

mycur   = conn.cursor() # Creating my cursor

question = raw_input("What room number are you looking for? ") # Querying the user for the room they want.

mycur.execute ("SELECT * FROM rooms WHERE room_number = %r ", (question, )) # (query, ) makes the raw input a tuple I think which is required here for the cursor

print mycur.fetchone()




#answer = mycur.execute ("SELECT * FROM rooms WHERE room_number = %s ", (question)) # (query) works for single entries but error message on more, no error message with [query] but doesnt work


#if answer == True:
    #print mycur.fetchone()
    
#elif question == False:
    #print "Sorry I couldn't find that room number!"

#else:
    #print "That seems to have not worked..."

  
mycur.close()
conn.close()