import mysql.connector 
 
db = mysql.connector.connect( 
  host="rebeccaf1918.mysql.pythonanywhere-services.com", 
  user="rebeccaf1918", 
  password="RootRoot", 
  database="rebeccaf1918$taylorsongs" 
) 
 
cursor = db.cursor() 
sql="insert into songs (title, album, genre, charting) values (%s,%s,%s,%s)" 
values = ("Sparks Fly","Speak Now", "Pop", 2) 
 
cursor.execute(sql, values) 
 
db.commit() 
print("1 record inserted, ID:", cursor.lastrowid) 
cursor.close() 
connection.close() 