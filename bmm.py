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
    errors  = ""
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
        
        mycur.fetchone()
        #errors = mycur.fetchwarnings()
        for i in mycur:
            room_number = i[0]
            room_name = i[1]
            room_description = i[2]
            
        #return mycur.fetchone()   #WORKING ONE!
            
        return """
        <html><head>
            <title>%s</title>
        </head>
        <body>
            <h1>%s: %s</h1>
            <hr>
            Room Details:<br>
            %s <br>
        </body>
        </html>
        """ % (room_name.upper(), room_number, room_name, room_description)
    
    elif answer == 0:
        return """
        <html><head>
            <title>No Results!</title>
        </head>
        <body>
            <h1>No Results Found!</h1>
            <hr>
            Sorry no results were returned, try a different search please!<br>           
        </body>
        </html>
        """

    else:
        return """
        <html><head>
            <title>Error</title>
        </head>
        <body>
            <h1>Error!!</h1>
            <hr>
            Sorry but we seem to have encountered an error!<br>
			%s <br>
        </body>
        </html>
        """ % (errors)

    mycur.close()
    conn.close()
