import csv      # Import the csv module
import MySQLdb  # Import MySQLdb module

host    = 'localhost'
user    = 'mo'
passwd  = 'muirwood'
db      = 'test'
    
conn    = MySQLdb.connect(host='localhost', # Connect to test database
                       user='mo', 
                       passwd='muirwood', 
                       db= 'test') 

mycur   = conn.cursor() # Creating my cursor

# creates a 'rooms' list, with reader function of csv module
# each row of the csv is made into it's own list with elements
rooms = csv.reader(file('list.txt')) 

for room in rooms: 			#for each list in the list rooms
    
    room_number = room[0] 	#pulls first element of each list and assigns to room_number variable
    region      = room[1] 	#pulls second element of each list and assigns to region variable


    # Inserts the room number and reqion into the rooms table in the test database.
    mycur.execute("""INSERT INTO rooms VALUES (%r, %r)""", (room_number, region))

conn.commit()   # Commit the changes to the table
mycur.execute("SELECT * FROM rooms")
print mycur.fetchall()