import csv                  # Import csv module
import MySQLdb              # Import MySQLdb module
import os                   # Import os


def index():

    return """
    <html><head>
        <title>British Museum Map Project</title>
    </head>
        <body>
            <h1>British Museum Map Project</h1>
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
    answer = mycur.execute ("SELECT room_number, room_name, room_description FROM rooms WHERE (room_number LIKE %r or room_name LIKE %r or room_tag1 LIKE %r or room_tag2 LIKE %r or room_tag3 LIKE %r)", ("%"+query+"%","%"+query+"%","%"+query+"%","%"+query+"%","%"+query+"%"))
    if answer >=1:
        
        mycur.fetchall()
        for i in mycur:
            room_number = i[0].strip('"\'')
            room_name = i[1].strip('"\'')
            room_description = i[2].strip('"\'')
            html = html + "<h1>" + room_number + ": " + room_name + "</h1><hr/>Room Details:<br/>" + room_description
            
        #return mycur.fetchone()   #WORKING ONE!
            
        
    elif answer == 0:
        html = "Sorry no results were returned, try a different search please!<br>"

    else:
        html = "Sorry but we seem to have encountered an error!<br>"

    mycur.close()
    conn.close()

    html = "<html><head><meta charset=\"UTF-8\"></meta><title>BMM</title></head><body>"+html+"</body></html>"
    
    return html