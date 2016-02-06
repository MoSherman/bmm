import csv                  # Import csv module
import MySQLdb              # Import MySQLdb module
import os                   # Import os
import urlparse             # Import URL parser
from mod_python import apache


def index():

    return """
    <html><head>
        <title>BMM</title>
    </head>
        <body>
            <h1>BMM</h1>
            <h3>Search below for a room or object within the museum:</h3>
            <FORM value="form" action="bmm.py/get_info" method="post">
                <P>
                    <LABEL for="search">Search: </LABEL>
                    <INPUT type="search" name="search"><BR>
                    <INPUT type="submit" value="Search"> <INPUT type="reset">
                </P>
            </FORM>
        </body>
    </html>
    """

def get_info(req):
    
    info    = req.form
    query   = info['search'] #assigning variable query to whatever the user inputs
    
    path    = os.path.expanduser('~/bmm_login.txt') # Specifying path to login details
    login   = csv.reader(file(path)) # Creating a list of the login details                                       
    html    = ""
    
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
    #answer = mycur.execute ("SELECT room_number, room_name, room_description FROM rooms WHERE (room_number LIKE %r or room_name LIKE %r or room_tag1 LIKE %r or room_tag2 LIKE %r or room_tag3 LIKE %r)", ("%"+query+"%","%"+query+"%","%"+query+"%","%"+query+"%","%"+query+"%"))
    answer = mycur.execute ("SELECT room_number, room_name FROM rooms WHERE (room_number LIKE %r or room_name LIKE %r or room_tag1 LIKE %r or room_tag2 LIKE %r or room_tag3 LIKE %r)", ("%"+query+"%","%"+query+"%","%"+query+"%","%"+query+"%","%"+query+"%"))

    if answer >=1:
        
        mycur.fetchall()
        for i in mycur:
            room_number = i[0].strip('"\'')
            room_name = i[1].strip('"\'')
            #room_description = i[2].strip('"\'')
            #html = html + "<h1>" + room_number + ": " + room_name + "</h1><hr/>Room Details:<br/>" + room_description
            html = html +  "<tr><td><a href=" + "get_room?=" + room_number + ">" + room_number + "</a></td><td><a href=" + "get_room?=" + room_number + ">" + room_name + "</a></td></tr>"
            
        #return mycur.fetchone()   #WORKING ONE!
            
        
    elif answer == 0:
        html = "Sorry no results were returned, try a different search please!<br>"

    else:
        html = "Sorry but we seem to have encountered an error!<br>"

    mycur.close()
    conn.close()

    html = "<html><head><meta charset=\"UTF-8\"></meta><meta name=\"viewport\" content=\"width=device-width, initial-scale=1\"></meta><link rel=\"stylesheet\" href=\"http://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css\"><script src=\"https://ajax.googleapis.com/ajax/libs/jquery/1.12.0/jquery.min.js\"></script><script src=\"http://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/js/bootstrap.min.js\"></script><title>BMM Result</title></head><body>\"<div class=\"container\"><h1> Rooms: </h1><table class=\"table table-hover\"><thead><tr><th>Room Number</th><th>Room Name</th></tr></thead><tbody>"+html+"</tbody></table></div></body></html>"
    
    return html

def get_room(req):
    
    html            = ""
    querystring     = req.parsed_uri[apache.URI_QUERY]
    room_number     = querystring.strip('=')
    
    #return room_number
    
    path    = os.path.expanduser('~/bmm_login.txt') # Specifying path to login details
    login   = csv.reader(file(path)) # Creating a list of the login details 
    
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
    
    #result  = mycur.execute ("SELECT room_number, room_name, room_description FROM rooms WHERE room_number = %r"), (room_number)
    result  = mycur.execute ("SELECT room_number, room_name, room_description FROM rooms WHERE room_number = %r", room_number)

    
    mycur.fetchone()
    
    for i in mycur:
        room_number = i[0].strip('"\'')
        room_name = i[1].strip('"\'')
        room_description = i[2].strip('"\'')
        html = html + "<h1>" + room_number + ": " + room_name + "</h1><hr/>Room Details:<br/>" + room_description
    
    mycur.close()
    conn.close()
    
    html = "<html><head><meta charset=\"UTF-8\"></meta><title>BMM</title></head><body>"+html+"</body></html>"
    
    return html