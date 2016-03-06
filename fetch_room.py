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

answer = mycur.execute ("SELECT * FROM rooms WHERE room_number = %r ", (question, )) # (query, ) makes the raw input a tuple I think which is required here for the cursor

if answer == True:
    print mycur.fetchone()
    
elif answer == False:
    print "Sorry I couldn't find that room number!"

else:
    print "That seems to have not worked..."

    
query = raw_input("What room are you looking for? ") # Querying the user for the room they want.

#answer = mycur.execute ("SELECT room_number, room_name FROM rooms WHERE (room_number LIKE '%%%r%%' or room_name LIKE '%%%r%%' or room_tag1 LIKE '%%%r%%' or room_tag2 LIKE '%%%r%%' or room_tag3 LIKE '%%%r%%')", (query,query,query,query,query))
#answer = mycur.execute ("SELECT room_number, room_name FROM rooms WHERE (room_number LIKE '%%r%' or room_name LIKE '%%r%' or room_tag1 LIKE '%%r%' or room_tag2 LIKE '%%r%' or room_tag3 LIKE '%%r%')", (query,query,query,query,query))
#answer = mycur.execute ("SELECT room_number, room_name FROM rooms WHERE (room_number LIKE %r or room_name LIKE %r or room_tag1 LIKE %r or room_tag2 LIKE %r or room_tag3 LIKE %r)", (query,query,query,query,query))
#answer = mycur.execute ("SELECT room_number, room_name FROM rooms WHERE CONTAIN ((room_number, %r) or (room_name, %r) or (room_tag1, %r) or (room_tag2, %r) or (room_tag3, %r))", (query,query,query,query,query))
answer = mycur.execute ("SELECT room_number, room_name FROM rooms WHERE (room_number LIKE %r or room_name LIKE %r or room_tag1 LIKE %r or room_tag2 LIKE %r or room_tag3 LIKE %r)", ("%"+query+"%","%"+query+"%","%"+query+"%","%"+query+"%","%"+query+"%"))


if answer == True:
    print mycur.fetchone()
    
elif answer == False:
    print "Sorry I couldn't find that room!"
	
elif len(query) != 2:
    print "Sorry I need more information than that! Please put in more then two characters!"	

else:
    print "That seems to have not worked..."


  
mycur.close()
conn.close()