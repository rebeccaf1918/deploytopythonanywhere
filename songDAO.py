#TODO 
# add in here from 7.02 lecture with song details in code to check it works
# then when further on can look at using it from python anywhere 
# when including dbconfig code in file, it will take in empty table as in lecture 


# This songDAO file contains the functions that will be used by the Application to interact with the song Database

import mysql.connector
import dbconfig as cfg

class songDAO:    # Defining the class for accessing the song data contained in the database &
    connection =""      # initialising the class variables
    cursor =""
    host =""
    user =""
    password =""
    database =""
    
    def __init__(self):
        self.host=       cfg.mysql['host']
        self.user=       cfg.mysql['user']
        self.password=   cfg.mysql['password']
        self.database=   cfg.mysql['database']

    def getcursor(self): 
        self.connection = mysql.connector.connect(
            host=       self.host,
            user=       self.user,
            password=   self.password,
            database=   self.database,
        )
        self.cursor = self.connection.cursor()
        return self.cursor

    def closeAll(self):     # closing the database object and cursor 
        self.connection.close()
        self.cursor.close()


   