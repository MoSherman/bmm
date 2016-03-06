import csv                  # Import csv module
import MySQLdb              # Import MySQLdb module
import os                   # Import os
import urlparse             # Import URL parser
from mod_python import apache

html_head = """
<html lang="en">
<head>
  <title>BMM</title>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.0/jquery.min.js"></script>
  <script src="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/js/bootstrap.min.js"></script>
  <style>
    html,body {
    height: 100%
    }
    
    /* Remove the navbar's default margin-bottom and rounded borders */ 
    .navbar {
      margin-bottom: 0;
      border-radius: 0;
    }
    
    .bg-3 {
      height:100vh;  
      padding-top: 100px;  
      background-color: #f2f2f2;
      font-size: 20px;  
      padding-bottom: 400px;
    }
    
    footer {
      margin-bottom: 0;
      margin-top: 0;  
      background-color: #000000;
      padding: 25px;
      color: #f2f2f2;  
    }
      
  </style>
</head>
<body>
<nav class="navbar navbar-inverse">
  <div class="container-fluid">
    <div class="navbar-header">
      <button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#myNavbar">
        <span class="icon-bar"></span>
        <span class="icon-bar"></span>
        <span class="icon-bar"></span>                        
      </button>
      <a class="navbar-brand" href="search">British Museum Map</a>
    </div>
    <div class="collapse navbar-collapse" id="myNavbar">
      <ul class="nav navbar-nav">
        <li><a href="search">Search</a></li>
        <li><a href="rooms_all">Room List</a></li>        
        <li><a href="https://www.britishmuseum.org/PDF/pdfA4_allfloors.pdf" target="_blank">Map</a></li>
        <li><a href="about">About</a></li>    
      </ul>
      <ul class="nav navbar-nav navbar-right">
        <li><a href="https://github.com/MoSherman/bmm" target="_blank"> GitHub Repo</a></li>
      </ul>
    </div>
  </div>
</nav>
"""

html_footer = """
<footer class="container-fluid text-center">
  <p>Copyright &copy; Moriah Sherman 2016</p>
</footer>
</body>
</html>
"""

def search():

    return html_head + """
    <div class="container-fluid bg-3 text-center">    
    <h1>Search for a Room</h1><br>   
    <FORM value="form" action="get_info" method="post">
         <P>            
            <INPUT type="search" name="search"><BR>
            <INPUT type="submit" value="Search"> 
         </P>
    </FORM>  
    </div> 
    """ + html_footer

def about():

    return html_head + """
    <div class="container-fluid bg-3 text-center">    
    <h1>British Museum Map Project</h1><br>
    <div class="col-sm-2"> 
    </div>
    <div class="col-sm-8"> 
        <p class=text-justify>This project is an ongoing attempt to provide an easily searchable index of the British Museum\'s rooms. This project uses a Bootstrap template to be accesable to both desktop and mobile users. The backend runs on a MySQL database with Python functions serving the information searched for. Future iterations of the project will hopefully include an Museum Object Search, images of rooms and objects, more detailed descriptions, and improved aesthetics. The code for this project can be viewed at my <a href="http://GitHub.com/MoSherman/bmm" target="_blank">GitHub.com bmm repository</a>. All information pertaining to the museum itself is the Copyright &copy; of Trustees of the British Museum.</p>
    </div>
    <div class="col-sm-2"> 
    </div>
    </div>
    </body>
    </html>
    """

def rooms_all():
    path    = os.path.expanduser('~/moriah/bmm_private/server_bmm_login.txt') # Specifying path to login details
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
    answer = mycur.execute ("SELECT room_number, room_name FROM rooms")
    
    mycur.fetchall()
    for i in mycur:
        room_number = i[0].strip('"\'')
        room_name = i[1].strip('"\'')
        #room_description = i[2].strip('"\'')
        #html = html + "<h1>" + room_number + ": " + room_name + "</h1><hr/>Room Details:<br/>" + room_description
        html = html +  "<tr><td><a href=" + "get_room?=" + room_number + ">" + room_number + "</a></td><td><a href=" + "get_room?=" + room_number + ">" + room_name + "</a></td></tr>"

    mycur.close()
    conn.close()

    html = html_head + "<html><head><meta charset=\"UTF-8\"></meta><meta name=\"viewport\" content=\"width=device-width, initial-scale=1\"></meta><link rel=\"stylesheet\" href=\"http://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css\"><script src=\"https://ajax.googleapis.com/ajax/libs/jquery/1.12.0/jquery.min.js\"></script><script src=\"http://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/js/bootstrap.min.js\"></script><title>BMM Result</title></head><body>\"<div class=\"container\"><h1> Rooms: </h1><table class=\"table table-hover\"><thead><tr><th>Room Number</th><th>Room Name</th></tr></thead><tbody>"+html+"</tbody></table></div></body></html></body></html>"
    
    return html    
        
def get_info(req):
    
    info    = req.form
    query   = info['search'] #assigning variable query to whatever the user inputs
    
    path    = os.path.expanduser('~/moriah/bmm_private/server_bmm_login.txt') # Specifying path to login details
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

    html = html_head + "<html><head><meta charset=\"UTF-8\"></meta><meta name=\"viewport\" content=\"width=device-width, initial-scale=1\"></meta><link rel=\"stylesheet\" href=\"http://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css\"><script src=\"https://ajax.googleapis.com/ajax/libs/jquery/1.12.0/jquery.min.js\"></script><script src=\"http://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/js/bootstrap.min.js\"></script><title>BMM Result</title></head><body>\"<div class=\"container\"><h1> Rooms: </h1><table class=\"table table-hover\"><thead><tr><th>Room Number</th><th>Room Name</th></tr></thead><tbody>"+html+"</tbody></table></div></body></html></body></html>"
    
    return html

def get_room(req):
    
    html            = ""
    querystring     = req.parsed_uri[apache.URI_QUERY]
    room_number     = querystring.strip('=')
    
    #return room_number
    
    path    = os.path.expanduser('~/moriah/bmm_private/server_bmm_login.txt') # Specifying path to login details
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
        #html = html + "<h1>" + room_number + ": " + room_name + "</h1><hr/>Room Details:<br/>" + room_description
        html = html + "<div class=\"container-fluid bg-3 text-center\"><h1>Room " + room_number + ": " + room_name + "</h1><div class=\"row\"><div class=\"col-sm-2 text-justify\"></div><div class=\"col-sm-8 text-justify\"><p>" + room_description + "</p></div><div class=\"col-sm-2 text-justify\"></div></div></div>"
                
    mycur.close()
    conn.close()
    
    html = html_head + html + "</body></html>"
    
    return html
