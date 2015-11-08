import csv #importing csv module to read list.txt file

# creates a 'rooms' list, with reader function of csv module
# each row of the csv is made into it's on list with elements
rooms = csv.reader(file('list.txt')) 

for room in rooms: 			#for each list in the list rooms
    
    room_number = room[0] 	#pulls first element of each list and assigns to room_number variable
    region      = room[1] 	#pulls second element of each list and assigns to region variable
    
    print room_number 		# displays the first element of every list (row) in the csv
    print region 			# displays the second element of every list (row) in the csv