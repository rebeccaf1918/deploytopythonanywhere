#TODO 
# add in here from 7.02 lecture with song details in code to check it works
# then when further on can look at using it from python anywhere 
# add in error handling


# This songDAO file contains the functions that will be used by the Application to interact with the song Database

import mysql.connector
import dbconfig as cfg
from mysql.connector import cursor
from mysql.connector.errors import Error
import sys


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

    def createDBtable(self): #creates the table if it does not already exist
        try:
            sql = """CREATE TABLE IF NOT EXISTS TaylorSwiftSongs (
                        id INT AUTO_INCREMENT PRIMARY KEY,
                        Title VARCHAR(250),
                        Album VARCHAR(250),
                        Genre VARCHAR(250),
                        Charting int
                    )"""
            self.cursor.execute(sql)
            self.connection.commit()
        except mysql.connector.Error as e:
            print(f"Error creating table: {e}")


    def getAll(self):
        cursor = self.getcursor()
        sql="SELECT * FROM TaylorSwiftSongs" #sql language to get all data from table
        cursor.execute(sql)
        results = cursor.fetchall()
        returnArray = []
        #print(results)
        for result in results:
            returnArray.append(self.convertToDictionary(result))
        self.closeAll()
        return returnArray
    
    
    def findByID(self, ID):
        try:
            cursor = self.getcursor()
            sql="SELECT * FROM TaylorSwiftSongs WHERE ID = %s"
            values = (ID,)
            cursor.execute(sql, values)
            result = self.cursor.fetchone()
            returnvalue = self.convertToDictionary(result)
            self.closeAll()
            return returnvalue
        except mysql.connector.Error as e:
            print(f"Error finding recipe: {e}")
            return None


    def create(self, SONG):
        cursor = self.getcursor()
        sql="INSERT INTO TaylorSwiftSongs (Title, Album, Genre, Charting) values (%s,%s,%s,%s)"
        values = (SONG.get("Title"), SONG.get("Album"), SONG.get("Genre"), SONG.get("Charting"))
        cursor.execute(sql, values)

        self.connection.commit()
        newID = cursor.lastrowid
        SONG["ID"] = newID
        self.closeAll()
        return SONG


    def update(self, ID, SONG):
        cursor = self.getcursor()
        sql="UPDATE taylorswiftsongs set Title= %s, Album=%s, Genre=%s, Charting=%s where ID = %s"
        print(f"update TaylorSwiftSongs {SONG}")
        values = (SONG.get("Title"), SONG.get("Album"), SONG.get("Genre"), SONG.get("Charting"), ID) 
        cursor.execute(sql, values)
        self.connection.commit()
        self.closeAll()

        
    def delete(self, ID):
        cursor = self.getcursor()
        sql="DELETE FROM TaylorSwiftSongs where ID = %s"
        values = (ID,)

        cursor.execute(sql, values)

        self.connection.commit()
        self.closeAll()
        print("Delete Completed")
    
    
    def findByGenre(self, Genre):
        cursor = self.getcursor()
        sql="SELECT * FROM TaylorSwiftSongs Where Genre = %s"
        values = (Genre,)

        cursor.execute(sql, values)
        results = cursor.fetchall()
        returnArray = []
        print(results)
        for result in results:
            returnArray.append(self.convertToDictionary(result))
        return returnArray
    
    def convertToDictionary(self, resultLine):
        attkeys=['ID', 'Title', 'Album','Genre', 'Charting']
        SONGS = {} #empty dict 
        currentkey = 0
        for attrib in resultLine:
            SONGS[attkeys[currentkey]] = attrib
            currentkey = currentkey + 1 
        return SONGS

        
songDAO = songDAO()