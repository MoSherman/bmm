""" This python script contains functions to open a connection to the bmm MySQL database.
    
    This script is a part of the British Museum Map Project aka bmm. For more on the project see:
    https://github.com/MoSherman/bmm
    
    This is version 1.0 started on Sun Nov 22 16:40:21 GMT 2015.
"""

import os       # Import os module
import csv      # Import csv module
import MySQLdb  # Import MySQLdb module

def connect():
    
    path    = os.path.expanduser('~/Projects/bmm_private/login_test.txt')
    login   = csv.reader(file(path))     
    
    #login   = csv.reader(file('/Projects/bmm_private/login_test.txt')) # Retrieve login details from secure file

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
    
    #mycur   = conn.cursor() # Creating my cursor