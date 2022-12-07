####### WAIKIRIKIRI LIBRARY MANAGEMENT SYSTEM #######
# Name:  Fei Wang
# Student ID: 1153888
####################################################

import mysql.connector
from mysql.connector import FieldType
import datetime
import connect_library
import re

dbconn = None

def getCursor():
    global dbconn
    global connection
    connection = mysql.connector.connect(
        user=connect_library.dbuser, 
        password=connect_library.dbpass, 
        host=connect_library.dbhost,
        database=connect_library.dbname, 
        autocommit=True
    )
    dbconn = connection.cursor()
    return dbconn


def columnOutput(dbData,cols,formatStr):
# dbData is a list of tuples
# cols is a dictionary with column name as the key and data type as the item
# formatStr uses the following format, with one set of curly braces {} for each column.
# For each column "{: <10}" determines the width of the column, padded with spaces (10 spaces in this example)
#   <, ^ and > determine the alignment of the text: < (left aligned), ^ (centre aligned), > (right aligned)
#   The following example is for 3 columns of output: left-aligned, 5 characters wide; centred, 10 characters; right-aligned 15 characters:
#       formatStr = "{: <5}  {: ^10}  {: >15}"
# You can also pad with something other than a space and put characters between the columns, 
# e.g. this pads with full stops '.' and separates the columns with the pipe character | :
#       formatStr = "{:.<5} | {:.^10} | {:.>15}"
    print(formatStr.format(*cols))
    for row in dbData:
        rowList=list(row)
        for index,item in enumerate(rowList):
            if item==None:      # Removes any None values from the rowList, which would cause the print(*rowList) to fail
                rowList[index]=""       # Replaces them with an empty string
            elif type(item)==datetime.date or type(item)==datetime.datetime or type(item)==datetime.time or type(item)==datetime.timedelta:    # If item is a date, date-time, time or timedelta, convert to a string to avoid formatting issues
                rowList[index]=str(item)
        print(formatStr.format(*rowList))   


def get_valid_value(input_value, expected_type):
    try:
        input_value = expected_type(input_value)
    except Exception as e:
        print(f"The value {input_value} if not a valid type of {expected_type}")
        input_value = None
    finally:
        return input_value


def listBooks():
    cur = getCursor()
    # book list with number of copy orderd by year of publication desc and then category asc and then title asc
    # number of copy will be 0 if there is no copy of a book
    cur.execute("select b.bookid, b.booktitle, b.category, b.yearofpublication, count(bc.bookid) as copynumber from books b left join bookcopies bc on b.bookid = bc.bookid group by b.bookid order by b.yearofpublication desc, b.category, b.booktitle;")
    dbOutput = cur.fetchall()
    colOutputDict = {desc[0]:FieldType.get_info(desc[1]) for desc in cur.description}  # creates a dictionary with column name as the key and data type as the item
    print("\nBOOKS\n")
    formatStr = "{: <7}  {: <50}  {: <20}  {: <20}  {: <10}"    # See columnOutput function for details on formatting options
    columnOutput(dbOutput,colOutputDict,formatStr)


def listBorrowers():
    cur = getCursor()
    # show all borrowers with the order of familiname asc and then firstname asc
    cur.execute("select * from borrowers order by familyname, firstname;")
    dbOutPut = cur.fetchall()
    colOutputDict = {desc[0]:FieldType.get_info(desc[1]) for desc in cur.description}
    print("\nBORROWERS\n")
    formatStr = "{: <15}  {: <10}  {: <10}  {: <15}  {: <20}  {: <20}  {: <15}  {: <15}  {: <15}"
    columnOutput(dbOutPut, colOutputDict, formatStr)


def listBookcopies(bookid=None):
    cur = getCursor()
    # show all book copies of specific bookid
    if bookid:
        querySql = "select * from bookcopies where bookid = %s"
        cur.execute(querySql, (bookid, ))
    else:
        querySql = "select * from bookcopies order by bookid, bookcopyid"
        cur.execute(querySql)
    dbOutput = cur.fetchall()
    colOutputDict = {desc[0]:FieldType.get_info(desc[1]) for desc in cur.description}
    print("\nBORROWERS\n")
    formatStr = "{: <15}  {: <10}  {: <20}"
    columnOutput(dbOutput, colOutputDict, formatStr)


def getNewValue(dbCur):
    columnNames = [desc[0] for desc in dbCur.description]
    displayText = ""
    for index in range(1, len(columnNames)):
        displayText += f"{index} - {columnNames[index]}\n"
    displayText += "0 <-Back\nPlease select the column INDEX to be updated: "
    # print the existed value to select from.
    columnIndex = get_valid_value(input(displayText), int)
    
    # columnIndex is not a valid value, or 0 for go back
    if not columnIndex or columnIndex == 0:
        return

    # Valid index
    if 0 < columnIndex < len(columnNames):
        columnName = columnNames[columnIndex]
        columnType = FieldType.get_info(dbCur.description[columnIndex][1])
        newValue = input("Please enter the value: ")
        if columnType == 'DATE':
            # A simplified expression to check date format. There should be a more exact pattern. 
            if re.search('^[0-9]{4}-[0-9]{2}-[0-9]{2}$', newValue):
                newValue = f"str_to_date('{newValue}', '%Y-%m-%d')"
            else:
                raise ValueError("Date value should be in format of 'yyyy-mm-dd'")
        else:
            newValue = f"'{newValue}'"
        # return a value that can be used in SQL statement immediately(with quotes).
        return columnName, newValue
    else:
        raise ValueError("The index you entered is not valid.")


def updateBorrower():
    # list all borrowers
    listBorrowers()
    # get user intpu borrower id
    borrower_id = get_valid_value(input("Please enter the borrower id you want update: "), int)
    if not borrower_id:  # borrower id is not a valid value
        return
    # fetch data from db of the specific borrower id
    cur = getCursor()
    cur.execute("select * from borrowers where borrowerid = %s", (borrower_id, ))
    dbOutPut = cur.fetchall()
    if dbOutPut:  # borrower id is valid
        try:
            columnName, newValue = getNewValue(cur)  # call a function to get valid column name and value
            updateSql = f"update borrowers set {columnName} = {newValue} where borrowerid = {borrower_id}"
            cur.execute(updateSql)  # execute the update SQL
            print("Value has been updated.")  # print result to user
        except ValueError as e:
            print(e)
        except Exception:
            return
    else:  # borrower id does not exist
        print("There is no such borrower.")


def addLoan():
    # enter borrower id and check if it is valid
    listBorrowers()
    cur = getCursor()
    borrowerid = get_valid_value(input("Please enter the borrower id: "), int)
    if not borrowerid:
        return
    cur.execute("select * from borrowers where borrowerid = %s", (borrowerid, ))
    dbOutput = cur.fetchall()
    if not dbOutput:
        print(f"The borrower id {borrowerid} does not exist.")
        return
    
    # enter book copy id and check if it is valid
    listBookcopies()
    cur = getCursor()
    bookcopyid = get_valid_value(input("Please enter the book copy id: "), int)
    if not bookcopyid:
        return
    cur.execute("select * from bookcopies where bookcopyid = %s", (bookcopyid, ))
    dbOutput = cur.fetchall()
    if not dbOutput:
        print(f"The book copy id {bookcopyid} does not exist.")
        return

    # insert a record of book loan
    cur = getCursor()
    cur.execute("insert into loans values(null, %s, %s, curdate(), 0)", (bookcopyid, borrowerid))
    print("Add loan finished.")


def reportOverdueBooks():
    # get overdue books
    sql = "select b.booktitle, br.firstname, br.familyname, curdate()-l.loandate as numberofdays from books b inner join bookcopies bc on b.bookid=bc.bookid inner join loans l on bc.bookcopyid=l.bookcopyid inner join borrowers br on br.borrowerid = l.borrowerid where curdate()-l.loandate>35 and l.returned=0"
    cur = getCursor()
    cur.execute(sql)
    dbOutput = cur.fetchall()
    colOutputDict = {desc[0]:FieldType.get_info(desc[1]) for desc in cur.description}
    print("\nOVERDUE\n")
    formatStr = "{: <50}  {: <10}  {: <10}  {: <15}"
    columnOutput(dbOutput,colOutputDict,formatStr)


def reportMostLoanedBooks():
    # list all loaned books order by times desc
    sql = "select b.bookid, b.booktitle, count(*) as borrowedtimes from books b, bookcopies bc, loans l where b.bookid = bc.bookid and bc.bookcopyid = l.bookcopyid group by b.bookid order by borrowedtimes desc"
    cur = getCursor()
    cur.execute(sql)
    dbOutput = cur.fetchall()
    colOutputDict = {desc[0]:FieldType.get_info(desc[1]) for desc in cur.description}
    print("\nOVERDUE\n")
    formatStr = "{: <10}  {: <50}  {: <10}"
    columnOutput(dbOutput,colOutputDict,formatStr)


#function to display the menu
def dispMenu():
    print("==== WELCOME TO WAIKIRIKIRI LIBRARY MANAGEMENT SYSTEM ===")
    print("1 - Book List")
    print("2 - Borrower List")
    print("3 - Update Borrower")
    print("4 - Overdue Books")
    print("5 - Most Loaned Books")
    print("6 - Loan Book")
    print("Q - Quit")
    response = input("Please select menu choice: ")
    return response.upper()  # Convert all entered content into UPPER case

# ******** MAIN PROGRAM *********

#Display the menu and prompt the user to select an item
response = dispMenu()

#repeat this loop until user enters a "Q"
while response != "Q":
    if response == "1":
        listBooks()
    elif response == "2":
        listBorrowers()
    elif response == "3":
        updateBorrower()
    elif response == "4":
        reportOverdueBooks()
    elif response == "5":
        reportMostLoanedBooks()
    elif response == "6":
        addLoan()
    elif response == "R":  # Option to continue the loop
        continue
    else:
        print("Invalid response, please re-enter.")

    input("\nPress Enter to continue.")
    #Display the menu and prompt the user to select an item
    response = dispMenu()

print("=== Thank you for using WAIKIRIKIRI LIBRARY MANAGEMENT SYSTEM ===")
