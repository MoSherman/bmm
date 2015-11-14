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

query = raw_input("What room are you looking for? ") # Querying the user for the room they want.

# Selecting the information to be queryed. 
answer = mycur.execute ("SELECT room_number, region FROM rooms WHERE (room_number == %r or region == %r)", query) 
print answer

#room = mycur.fetchone () # Fetches one row at a time from rooms table.

#if room[0] == query or room[1] == query:
    #print room
    
#else:
    #print "Sorry I couldn't find any rooms that matched your query!"
    
mycur.close()
conn.close()