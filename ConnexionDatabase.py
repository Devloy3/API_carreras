import mysql.connector

class ConnDatabase:
    def __init__(self,host,user,password,database):
        self.setHost(host)
        self.setUser(user)
        self.setPassword(password)
        self.setDatabase(database)
        
        self.mydb = mysql.connector.connect(
            host=self.getHost(),
            user=self.getUser(),
            password=self.getPassword(),
            database=self.getDatabase()
        )

        self.cursor = self.mydb.cursor()

    def setHost(self,host):
        self.__host = host
        
    def setUser(self,user):
        self.__user = user

    def setPassword(self,password):
        self.__password = password

    def setDatabase(self,database):
        self.__database = database

    def getHost(self):
        return self.__host
    
    def getPassword(self):
        return self.__password
    
    def getUser(self):
        return self.__user
    
    def getDatabase(self):
        return self.__database
    



        
    