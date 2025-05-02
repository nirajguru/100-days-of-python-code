import sqlite3

connection = sqlite3.connect("data.db")
cursor = connection.cursor()

# create a table
cursor.execute("CREATE TABLE USERS(ID INTERGER PRIMARY KEY, NAME TEXT, AGE INTEGER)")

# insert a record

cursor.execute("INSERT INTO USERS VALUES(1, 'John', 25)")
cursor.execute("INSERT INTO USERS VALUES(2, 'Jane', 30)")
cursor.execute("INSERT INTO USERS VALUES(3, 'Doe', 22)")
cursor.execute("INSERT INTO USERS VALUES(4, 'Alice', 28)")

# commit the changes
connection.commit()

# fetch all records
cursor.execute("SELECT * FROM USERS")

# print all records 
for row in cursor.fetchall():
    print(row)
    
# close the connection
connection.close()
