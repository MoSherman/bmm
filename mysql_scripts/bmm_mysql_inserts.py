""" This python script pulls data from a *.txt file and passes it to the bmm MySQL database.
    It's purpose is to automate the process of adding room information to the database.
    
    This script is a part of the British Museum Map Project aka bmm. For more on the project see:
    https://github.com/MoSherman/bmm
    
    This is version 1.0 started on Sun Nov 22 14:21:42 GMT 2015.
"""

import csv                  # Import the csv module
import MySQLdb              # Import MySQLdb module
import bmm_mysql_connect    # Import my connection module

bmm_mysql_connect.connect() # my attempt to import the mysql connection from a module, not sure if that runs the connection for the whole script

#login   = csv.reader(file('/~/Projects/bmm_private/bmm_login.txt')) # Retrieve login details from secure file

# Assign login details to connection variables
#host    = login[0]
#user    = login[1]
#passwd  = login[2]
#db      = login[3]

# Connect to test database
#conn    = MySQLdb.connect(host=host, 
                       user=user, 
                       passwd=passwd, 
                       db=db) 
    
#mycur   = conn.cursor() # Creating my cursor

#rooms = csv.reader(file('/~/Projects/bmm_private/bmm_room_list.txt')) # Retrieve bmm room data 

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


objects = csv.reader(file('/~/Projects/bmm_private/bmm_object_list.txt')) # Retrieve bmm object data

# Assign variables to each element in the bmm_object_list.txt
# Executes SQL command to INSERT the VALUES into the apropriate columns in the objects table of the bmm database
for item in objects:
    
    object_name         = item[0]
    object_description  = item[1]
    
        mycur.execute("INSERT INTO objects (object_name,object_description) VALUES (%r, %r)", 
                  (object_name,object_description))

conn.commit()   # Commit the changes to the table
conn.close()    # Close connection to bmm database  