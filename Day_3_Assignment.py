"""Author    : Shaik Salman Khan
   CreatedOn : Oct 23/2020
   Purpose   : Submitting Day_3 Programming assignment 	
"""

#----------------------------Program 1------------------------------------
# WAP to input Employee data(id,name,salary) for 10 employees in file emp.txt

#Creating a File named as emp.txt to store emp data
Emp_File   = open("emp.txt","w")

#Using a For loop to input 10 Employees Data
for i in range(1,11):

    #Asking user to Enter Employee Data
    Emp_Id     = int(input("Please Enter your ID Number : "))
    Emp_Name   =     input("Please Enter your Name : ")
    Emp_Salary = int(input("Please Enter your Salary : "))

    #printing Emp details in file
    Emp_File.write("Employee "+ str(i) + " Data " + "\n")

    #Using dashes to seperate emp information
    Emp_File.write("---------------------"+ "\n" )
    
    #Writing Data to the emp.txt
    Emp_File.write("ID    : " +  str(Emp_Id)+"\n")
    Emp_File.write("Name  : " +  Emp_Name +"\n")
    Emp_File.write("Salary: " +  str(Emp_Salary)+ "\n")

    #printing a space in emp.txt
    Emp_File.write("\n")
    
    #Printing File Saved
    print("File Saved for Employee " +str(i))

#After the For Loop closing the file
Emp_File.close()   


#----------------------------Program 2------------------------------------
# WAP to read data from emp.txt file

#Opening the emp.txt file to read emp data
Emp_File   = open("emp.txt","r")

#read all the info present in emp.text
Emp_Data   = Emp_File.read()

#printing the emp data
print(Emp_Data)

#closing the file
Emp_File.close()   


#----------------------------Program 3------------------------------------
# WAP to read the file and transfer only vowels in another file
#  (File name to be input by user)

"""[Note: i dont have any text file in the disk that'y i created a Letters File  ]
   [that contains all 26 letters]"""                                                                      


#------------------Creating The File----------------

#First creating a file that contains all 26 letters
Letters = open("Letters.txt","w")

#by using in built chr() func to get all letters from a to z
for letter in range(97,123):
    #Writing the data to the file
    Letters.write(chr(letter))

#Closing the File
Letters.close()

#------------------Reading The File----------------

#Reading the Letters.txt file which contains all letters i.e a to z
Letters     = open("Letters.txt","r")
All_Letters = Letters.read()


#--------------transfer only vowels in another file-----------------

#Asking User to Enter a File Name & writing only vowels to it
User_File_Name = input("Please Enter File Name of Your Choice : ")
File_Vowels    = open(User_File_Name + ".txt","w")


#Using a for loop to iterate over Letters File which contains 26 letters
for letter in All_Letters:
  
    #checking for all vowels i.e; [a,e,i,o,u]    
    if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u':
        #Writing all vowels to the file
        File_Vowels.write(letter)


#closing the Vowels file
File_Vowels.close()

#Closing the Letters file
Letters.close()



#----------------------------Program 4------------------------------------
# WAP to count the number of letters of any text file in the disk
# (input file name from user)

"""[Note: i dont have any text file in the disk to count number of letters ]
   [that'y i created a "Number_Letter_File" which contains both number & letter]"""                                                                      


#-------------[Creating the File with Numbers & letters]---------

#Create a file with both numbers & letters
Number_Letter_File = open("Number_Letter_File.txt","w")

#writing both numbers(97 to 26) & letters(a to z) to the file
for i in range(97,123):
    #using a inbuilt chr() func to get letters(a to z)
    Number_Letter_File.write(chr(i))
    #writing numbers
    Number_Letter_File.write(str(i))

#Closing the file which contains both letters & numbers
Number_Letter_File.close()


#-------------Reading the file to count only letters not numbers-----

#Reading the file which contains both Number(97 to 122) & letters(a to z)
Number_Letter_File      =  open("Number_Letter_File.txt","r")
Number_Letter_File_Read =  Number_Letter_File.read()

#Asking User to Enter a File Name & Creating the file with user entered name
User_File_Name    = input("Please Enter File Name of Your Choice : ")
Count_Letters     = open(User_File_Name + ".txt","w")
count             = 0

#using for loop to iterate over Number_Letter_File 
for i in Number_Letter_File_Read:
    #Checking file contains letter 
    if i.isalpha():
       #if File Contains letter then increment the counter  
        count = count + 1

#After the For Loop & write the counter value to User_File_Name
Count_Letters.write(str(count))

#Closing the file        
Number_Letter_File.close()
Count_Letters.close()

#----------------------------Program 5------------------------------------
# WAP to read emp.txt and print name of employee only..

#Opening the emp.txt file to read emp data
Emp_File   = open("emp.txt","r")

#Using a for loop to iterate over Emp_File
for line in Emp_File:
    #if line contains Name then
    if line.startswith("Name"):
        print(line,end='')

#closing the file
Emp_File.close()   







