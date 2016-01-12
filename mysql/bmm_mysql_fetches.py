""" This python script contains functions to fetch data from the bmm MySQL database.
    It's purpose is to allow a user to enter input and retrieve/print room and object information from the database.
    
    This script is a part of the British Museum Map Project aka bmm. For more on the project see:
    https://github.com/MoSherman/bmm
    
    This is version 1.0 started on Sun Nov 22 16:37:42 GMT 2015.
"""

import MySQLdb  # Import MySQLdb module 

# Retrieves room information from rooms table of bmm database after user input
def room_search():
    
    query = raw_input("What room are you looking for? ") # Querying the user for the room they want.
    
    # Selecting the information to be queryed. 
    answer = mycur.execute ("SELECT room_number, region FROM rooms WHERE (room_number = %r or region = %r or room_tag1 = %r or room_tag2 = %r or room_tag3 = %r)", (query,query,query,query,query)) 
    
    print answer

room_search()
