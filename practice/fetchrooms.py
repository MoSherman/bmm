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


query = raw_input("What room are you looking for? ") # Querying the user for the room they want.

answer = mycur.execute ("SELECT room_number FROM rooms WHERE room_number = %r ", (query))

print answer





# Selecting the information to be queryed. 
#answer = mycur.execute ("SELECT room_number, region FROM rooms WHERE (room_number = %r or region = %r)", (query,query)) 
#print answer

#rows = mycur.fetchall()
#for row in rows:
    #print row

#room = mycur.fetchone () # Fetches one row at a time from rooms table.

#if room[0] == query or room[1] == query:
    #print room
    
#else:
    #print "Sorry I couldn't find any rooms that matched your query!"
    
mycur.close()
conn.close()