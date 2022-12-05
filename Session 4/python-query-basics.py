import mysql.connector
#from mysql.connector import FieldType
import datetime
import connect_comp636

#connection = None
dbconn = None

def getCursor():
    global dbconn
    global connection
    connection = mysql.connector.connect(user=connect_comp636.dbuser, \
    password=connect_comp636.dbpass, host=connect_comp636.dbhost, \
    database=connect_comp636.dbname, autocommit=True)
    dbconn = connection.cursor()
    return dbconn

#########################################################################################################
# Run this code and follow the output in the terminal window and the corresponding lines of code below. #
#########################################################################################################

########## 1 ###########
cur = getCursor()
sql = "select * from people;"
cur.execute(sql)    # Executes the query
dbPeople = cur.fetchall()   # Passes the results of the query into a list of tuples
colsPeople = [desc[0] for desc in cur.description]  # creates a list of the column names
print()
print(sql)
print("\n1. The column names are in list colsPeople:")
print(colsPeople)
input("\nPress enter to continue each time you see '...'\n")

########## 2 ###########
input("\n2. The data is a list of tuples - dbPeople...")
print(dbPeople)
print("\nEach row from the database is a tuple in dbPeople (above).")
input("...\n")

########## 3 ###########
input("3. This is the first row...")
print(dbPeople[0])
print("   Look for it in dbPeople above.")
input("...\n")

########## 4 ###########
input("\n4. This is the second item in the third row (tuple)...")
print(dbPeople[2][1])
print("   Look for it in dbPeople above.")
input("...\n")

########## 5 ###########
input("\n5. This loops through each row (tuple) of the data and prints it on a new line...")
rowNum=0
for row in dbPeople:
    rowNum+=1
    print(f"Row {rowNum}: {row}")
input("...\n")

########## 6 ###########
input("\n6. This loops through each item in the last row of the data above...")
for item in dbPeople[90]:
    print(item)
input("...\n")

########## 7 ###########
input("7. Selecting a particular row and fields - passing a single parameter:  select name, city from people where id=1001...")
sql = "select name, city from people where id=%s;"      # The %s marker is a placeholder for the parameters to pass to the query
parameters = (1001,)    # The last comma tells Python this is a tuple with only one entry
cur.execute(sql,parameters)
dbPeople = cur.fetchall()
colsPeople = [desc[0] for desc in cur.description]  
print("   This now returns name and city in one row for person 1001:")
print(dbPeople)
input("\n...\n")

########## 8 ###########
input("8. Passing multiple parameters - 3 criteria:  select * from people where sex='F' and age<20 and weight>70")
sql = "select * from people where sex=%s and age<%s and weight>%s;"   # No quote marks '' needed - the connector works that out for you
parameters = ('F',20,70)    # Parameters are passed as a tuple, replacing the %s markers in the order they appear in the SQL string
cur.execute(sql,parameters)
dbPeople = cur.fetchall()
colsPeople = [desc[0] for desc in cur.description]  
for item in dbPeople:
    print(item)
input("...\n")

########## 9 ###########
print("9. Adding a new record - including primary key:  insert:  (577,'Ima', 'Newmember', 'Junior', '023-456-7890', 44, datetime.date(2004, 5, 8), 'Team C', 'M', 0)")
input("   This works the first time...")
isAnError=False
while not isAnError:
    sql = "INSERT INTO member VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"
    print(sql)
    parameters = (577,'Ima', 'Newmember', 'Junior', '023-456-7890', 44, datetime.date(2004, 5, 8), 'Team C', 'M', 0)    # Parameters are passed as a tuple.
    try:
        cur.execute(sql,parameters)     # Run the INSERT query
        sql = "select * from member;"   # See the results
        cur.execute(sql)
        dbMember = cur.fetchall()
        colsMember = [desc[0] for desc in cur.description]  
        print()
        print(sql)
        for item in dbMember:
            print(item)
        print("See the new record in the last row.")
        input("\nIt doesn't work the next time though...")
    except Exception as e:
        isAnError=True
        print(e)
        print("...because the primary key 577 is duplicated.")
    input("...\n")

########## 10 ###########
input("10. Adding a new record - using autoincrement of the primary key in the database")
print("    This time we can add the same row 3 more times and the member ID automatically increments due to the database configuration.")
input("    This avoids having to know what the next unique ID is.")
input(f"    We can now insert this row 3 times: {parameters}")
# To exclude the primary key, we now need to name each field which is being updated in the INSERT statement
sql = "INSERT INTO member(LastName,FirstName,MemberType,Phone,Handicap,JoinDate,MemberTeam,Gender,LifeMember) \
        VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s);"
parameters = ('Ima-Ima', 'Newmember-Again', 'Junior', '023-456-7890', 44, datetime.date(2000, 1, 1), 'Team C', 'M', 0)   
input("...")
for i in range(3):      # Add the same row 4 times
    cur.execute(sql,parameters)
sql = "select * from member;"       # Show the results
cur.execute(sql)
dbMember = cur.fetchall()
colsMember = [desc[0] for desc in cur.description]  
for item in dbMember:
    print(item)
print("Note the last 3 entries above - each has a different member ID.")
input("...\n")

input("11. Updating a record")
input("    This code loops through the handicap for each member.  Try changing some of the values...")
cur = getCursor()
cur.execute("select MemberID, FirstName, LastName, Handicap from member;")
dbMemberHandicap = list(cur.fetchall())     # This SELECT query gives us the name and handicap of each member to loop through
colsMemberHandicap = [desc[0] for desc in cur.description]  
for row in dbMemberHandicap:
    memberID=row[0]
    firstName=row[1]
    lastName=row[2]
    handicap=row[3]
# Or a shorthand which is exactly the same as the previous 3 lines of code:
for memberID,firstName,lastName,handicap in dbMemberHandicap:
    print(f"\nMember: {firstName} {lastName} - Current handicap: {handicap}")
    newHandicap=input("Enter a new value or leave blank to leave unchanged: ")
    if newHandicap!="":
        sql = "UPDATE member SET handicap=%s WHERE MemberID = %s;"
        parameters=(newHandicap,memberID)
        cur = getCursor()
        cur.execute(sql,parameters)
cur.execute("select MemberID, FirstName, LastName, Handicap from member;")
dbMemberHandicap = list(cur.fetchall())     # This SELECT query gives us the name and handicap of each member to loop through
print("\nThe updated handicaps:")
for item in dbMemberHandicap:
    print(item)
input("Your changes should now show in the results above.\n")

input("If you look in MySQL Workbench, you will see the changes that were made in this exercise are now stored in your database.\n")

print("\nIf you want to reset the data, re-run the SQL query that you used to create the COMP636 database.")


