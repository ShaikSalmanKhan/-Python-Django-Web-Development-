"""Author    : Shaik Salman Khan
   CreatedOn : Oct 28/2020
   Purpose   : Submitting Day_5 Programming assignment 	
"""

#----------------------------Programs------------------------------------
""" Maintain Data for stock management and
    maintain CRUD on table(dynamically input) on following

	ItemCategory
	itemcatid,catname,description(Varchar(20))

	Item
	ItemId,Iname,qty,price

	Customer
	cid,cname,email,itemid
"""

def Creating_db(db):
    """Used to Create New DATABASE """
    try:            
        Query_Creating_DB = 'create database %s'%(db)
        cursor.execute(Query_Creating_DB)
        print("Database successfully created")
        return True
            
    except mysql.connector.Error as err:
        print("Something went wrong",err.msg)


def show_table(Table_Name,Values_List_type):
    """Used To Show DATABASE Table"""

    #Showing the table to the user
    print("\tShowing the %s Table\n"%Table_Name)

    #iterating over Values_List_type to get header like id  name
    for i in Values_List_type:
        print('\t',i,end='')
    print("\n\t----------------------")

    #Executing cursor object to show all data present in table
    cursor.execute('select * from %s'%Table_Name)    
    rows = cursor.fetchall()            

    for row in rows:
        print("\t",row," ")
    print("\t----------------------")        


def CRUD(db):        
    """Used to Perform CRUD ON DATABASE"""
    try:
                use_db = 'use %s'%db
                cursor.execute(use_db)
                '--------------------CREATE---------------------------'
                #Creating table from user entered database
                Table_Name = input("\nPlease Enter your table Name : ")
                #Using a STRING to store Field Name & Field Type
                query_create = ''                
                #Asking user how many fields he want
                Field_number = int(input("\nHow many Fields you want in %s Table:"%(Table_Name)))
                print("\nBe Carefull to enter Field_Name & Field_Type(like: int,varchar(10))")
                
                #Using a Forloop to store Field_Name & Field_type in Table
                for i in range(Field_number):
                    Field_Name = input("\nField Name : ")
                    Field_Type = input("Field type : ")
                    query_create = query_create + Field_Name + " " + Field_Type+ ","
                    
                #making sql from user entered fields name & fields type                
                query_create = query_create[:-1]             
                Query_Creating_Table = 'create table %s(%s)'%(Table_Name,query_create)
            
                cursor.execute(Query_Creating_Table)
                print("\n\t %s Succesfully Created"%(Table_Name))
                #Showing the created table to the user
                Query_Showing_Table  = 'describe %s'%(Table_Name)
                cursor.execute(Query_Showing_Table)
                Showing_Table        =  cursor.fetchall()
                Values_List          =   []
                Values_List_type     =   []
                
                print("\n\t","Field","\t","Type")
                print("\t-----------------------")
                for i in Showing_Table:
                    print("\t",i[0],"\t",i[1])
                    Values_List.append(i[1])
                    Values_List_type.append(i[0])
                print("\t----------------------")
                

    
                '--------------------READ---------------------------'                
                #First insert values into the created table
                how_many_values = int(input("\nHow many Values to insert in %s Table:"%Table_Name))

                #Asking user how many values he want to insert in his table
                for value in range(how_many_values):
                    query_update = ''
                    for i in Values_List:
                        Value          = input("Please enter Value of "+ str(i)+ ":")
                        query_update   = query_update + Value + ","
                    
                    query_update = query_update[:-1]
                
                    #inserting values into database
                    Query_inserting_Table = 'insert into %s values(%s)'%(Table_Name,query_update)
                    cursor.execute(Query_inserting_Table)

                    #Saving it in database
                    database_connection.commit()

                #printing values inserted succesfully in table
                print("\n\tSuccesfully Inserted")
                    

                #Showing the table
                show_table(Table_Name,Values_List_type)
                
                
                '--------------------UPDATE---------------------------'
                print("\nFrom the above table Write a sql query to update")
                update_query = input("")
                cursor.execute(update_query)
                database_connection.commit()
                print("\n\tSucessfully updated")

                #Showing the table
                show_table(Table_Name,Values_List_type)
                
                '--------------------DELETE---------------------------'
                print("\nFrom the above table Write a sql query to Delete")
                delete_query = input("")
                cursor.execute(delete_query)
                database_connection.commit()
                print("\n\tSucessfully Deleted")

                #Showing the table
                show_table(Table_Name,Values_List_type)
                
                
    except mysql.connector.Error as err:
                print(err.msg)



#importing mysql.connector to connect to MySql database
import mysql.connector
from   mysql.connector import errorcode
#Creating connection with connect() method
database_connection  =   mysql.connector.connect(
                                                  host='localhost',
                                                  user='root',
                                                  password='root',
                                                 )
#Creating the cursor object
cursor        =  database_connection.cursor()
#Executing the cursor
cursor.execute('show databases')
#this list is used to store all database in the system
All_Database_List = []
#iterating over cursor to get all databases
for (i) in cursor:
    All_Database_List.append(i[0])

#Asking user if he want create a new database or use a existing database
Decision = input("Press yes to create a new DATABASE || Press No to use a existing Database: ").lower()
if Decision == 'yes':
    #Asking user to enter a Database Name
    User_Entered_db  = input("\nPlease Enter Your Database Name: ")    
    #Checking if User_Entered_db not in present in database list
    if User_Entered_db not in All_Database_List:

        #Calling the creating db func 
        if Creating_db(User_Entered_db):
            #Call the CRUD fun
            CRUD(User_Entered_db)
    else:
        print("Sorry DATABASE already exists.....Try again")                
elif Decision == 'no':

    #Asking user to enter his existing Database Name
    Existing_Database  = input("\nPlease Enter Existing Database Name: ")
    #if user entered db present in database list then only perform CRUD
    if Existing_Database in All_Database_List:

        print("Successfully entered into ",Existing_Database)
        #Call the CRUD func to perform C,R,U,D
        CRUD(Existing_Database)
    else:
        print("Sorry your DATABASE DOESN'T EXIST")                
else:
    print("You have entered a wrong input...Try again")


  


