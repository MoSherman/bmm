import MySQLdb

class Database:
    
    host    = 'localhost'
    user    = 'mo'
    passwd  = 'muirwood'
    db      = 'test'
    
    def __init__(self):
        self.connection = MySQLdb.commect ( host = self.host,
                                            user = self.user,
                                            passwd = self.passwd, 
                                            db = self.db )
    
    def 
