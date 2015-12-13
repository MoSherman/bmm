""" This python script pulls data from a *.txt file and passes it to the bmm MySQL database.
    It's purpose is to automate the process of adding room information to the database.
    
    This script is a part of the British Museum Map Project aka bmm. For more on the project see:
    https://github.com/MoSherman/bmm
    
    This is version 1.0 started on Sun Nov 22 14:21:42 GMT 2015.
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


path2 = os.path.expanduser('~/Projects/bmm_private/bmm_room_list.txt') # Specifying path to room details
rooms = csv.reader(file(path2)) # Creating a list of the room details 

# Assign variables to each element in the bmm_rooms_list.txt
# Executes SQL command to INSERT the VALUES into the apropriate columns in the rooms table of the bmm database
for room in rooms:
    
    room_number         = room[0]
    room_name           = room[1]
    room_tag1           = room[2]
    room_tag2           = room[3]
    room_tag3           = room[4]
    room_description    = room[5]
    
    mycur.execute("INSERT INTO rooms (room_number,room_name,room_tag1,room_tag2,room_tag3,room_description) VALUES (%r, %r, %r, %r, %r, %r)", 
                  (room_number,room_name,room_tag1,room_tag2,room_tag3,room_description))

conn.commit()   # Commit the changes to the table
conn.close()    # Close connection to bmm database  