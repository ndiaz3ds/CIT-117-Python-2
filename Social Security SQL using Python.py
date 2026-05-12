import sqlite3
import os

DB_NAME= "retirement.db"
def database_setup():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    #create tables for the data
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Employee (
        EmployeeID INTEGER PRIMARY KEY,
        Name TEXT
        )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS  Pay (
        EmployeeID INTEGER, 
        Year INTEGER,
        Earnings REAL
        )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS SocialSecurityMinimum (
        Year INTEGER PRIMARY KEY,
        Minimum REAL
        )
    ''')

    #prevent any dupes from being inserted
    cursor.execute("SELECT COUNT(*) FROM Employee")
    if cursor.fetchone()[0] == 0:
        #just importing the employee data
        if os.path.isfile('Employee.txt'):
            with open('Employee.txt', 'r') as file:
                next(file)
                for line in file:
                    data=line.strip().split(',')

                    cursor.execute('''
                    INSERT INTO Employee (EmployeeID, Name)
                                        VALUES (?,?)
                                    ''', (int(data[0]), data[1]))

    cursor.execute("SELECT COUNT(*) FROM Pay")
    if cursor.fetchone()[0] == 0:
        if os.path.isfile('Pay.txt'):
            with open('Pay.txt', 'r') as file:
                next(file)
                for line in file:
                    data=line.strip().split(',')

                    cursor.execute('''
                    INSERT INTO Pay (EmployeeID, Year, Earnings)
                    VALUES (?,?,?)
                ''', (int(data[0]),int(data[1]), float(data[2])))


    cursor.execute("SELECT COUNT(*) FROM SocialSecurityMinimum")

    if cursor.fetchone()[0] == 0:
        if os.path.isfile('SocialSecurityMinimum.txt'):
            with open('SocialSecurityMinimum.txt', 'r') as file:
                next(file)
                for line in file:
                    data=line.strip().split(',')

                    cursor.execute('''
                    INSERT INTO SocialSecurityMinimum (Year, Minimum)
                    VALUES (?,?)
                    ''', (int(data[0]), float(data[1])))


    conn.commit()

    return conn, cursor



def report(cursor):

    cursor.execute('''
    SELECT Employee.Name,
            Pay.Year,
            Pay.Earnings,
            SocialSecurityMinimum.Minimum,
            
            CASE
                WHEN Pay.Earnings >= SocialSecurityMinimum.Minimum 
                THEN 'Yes'
                ELSE 'No'
            END AS Include
            
    FROM Pay
    
    JOIN Employee
        ON Pay.EmployeeID = Employee.EmployeeID
        
    JOIN SocialSecurityMinimum
        ON Pay.Year = SocialSecurityMinimum.Year
    
    ORDER BY Employee.Name, Pay.Year
    ''')
    rows = cursor.fetchall()

    print(f"{'Employee Name':<20}{'Year':<8}{'Earnings':<15}{'Minimum':<15}{'Include'}")

    for row in rows:
        print(f"{row[0]:<20}{row[1]:<8}{row[2]:<15,.2f}{row[3]:<15,.2f}{row[4]}")



def main():
    conn, cursor = database_setup()

    report(cursor)

    conn.close()

main()





#Nicholas Diaz

#Reflection Questions

#What did I like?

#I liked the end result from coding this thing

#What did I struggle with?

#Honestly I struggled with coming up with writing the code to import the data properly

#What are decorations?

#Decorations are like trigger words that instruct python to treat code as strings, floats, or properties in python.

#What is DDL and DML and how did I use them?

#DML manipulates data and puts it in our output and DDL organizes and edits the data so it can be displayed. I used them both by using CREATE, JOIN, SELECT, INSERT INTO.

#How does the SQL SELECT JOIN work in my code?

#It works by having the employee ID be matched with the name of the employee then it determines wether their salary get them a pension.

#What did I learn?

#1. I reinforced my abilities of how to properly use SQL and set up data from a txt file into a table

#2. I learned how SQL is used in python and how it can be utilized
