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


path3 = os.path.expanduser('~/Projects/bmm_private/bmm_object_list.txt') # Specifying path to room details
objects = csv.reader(file(path3)) # Creating a list of the room details 

# Assign variables to each element in the bmm_object_list.txt
# Executes SQL command to INSERT the VALUES into the apropriate columns in the objects table of the bmm database
for item in objects:
    
    object_name         = item[0]
    object_description  = item[1]
    
        mycur.execute("INSERT INTO objects (object_name,object_description) VALUES (%r, %r)", 
                  (object_name,object_description))

conn.commit()   # Commit the changes to the table
conn.close()    # Close connection to bmm database  