""" This python script contains functions to open a connection to the bmm MySQL database.
    
    This script is a part of the British Museum Map Project aka bmm. For more on the project see:
    https://github.com/MoSherman/bmm
    
    This is version 1.0 started on Sun Nov 22 16:40:21 GMT 2015.
"""

import csv      # Import the csv module
import MySQLdb  # Import MySQLdb module

def connect():

    login   = csv.reader(file('/~/Projects/bmm_private/bmm_login.txt')) # Retrieve login details from secure file

    # Assign login details to connection variables
    host    = login[0]
    user    = login[1]
    passwd  = login[2]
    db      = login[3]

    # Connect to test database
    conn    = MySQLdb.connect(host=host, 
                        user=user, 
                        passwd=passwd, 
                        db=db) 
    
    mycur   = conn.cursor() # Creating my cursor