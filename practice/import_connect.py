#import bmm_mysql_connect    # Import my connection module
import csv                  
import MySQLdb 
import os

#bmm_mysql_connect.connect() # Connecting to mysql test database
#mycur = conn.cursor()       # Creating my cursor

path    = os.path.expanduser('~/Projects/bmm_private/login_test.txt')
login   = csv.reader(file(path))     

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

# creates a 'rooms' list, with reader function of csv module
# each row of the csv is made into it's own list with elements
rooms = csv.reader(file('list.txt')) 

for room in rooms: 			#for each list in the list rooms
    
    room_number = room[0] 	#pulls first element of each list and assigns to room_number variable
    region      = room[1] 	#pulls second element of each list and assigns to region variable


    # Inserts the room number and reqion into the rooms table in the test database.
    mycur.execute("INSERT INTO rooms VALUES (%r, %r)", (room_number, region))

conn.commit()   # Commit the changes to the table
mycur.execute("SELECT * FROM rooms")
print mycur.fetchall()