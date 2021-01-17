
"""Author    : Shaik Salman Khan
   CreatedOn : Oct 10/2020
   Purpose   : Submitting Day_1 Programming assignment 	
"""

#----------------------------Program 1------------------------------------
# Make a program to input name & marks of five subjects and Calculate the Percentage of it

#Asking user to enter his Name
Name       =  input("Please Enter Your Name : ")

#Asking user to enter marks of five subjects
Maths      =  int(input("Please Enter Your Maths Marks : "))
Physics    =  int(input("Please Enter Your Physics Marks : "))
Social     =  int(input("Please Enter Your Social Marks : "))
Science    =  int(input("Please Enter Your Science Marks : "))
Hindi      =  int(input("Please Enter Your Hindi Marks : "))

#Calculating the Total Marks
Total_Marks = Maths + Physics + Social + Science + Hindi

#Calculating the Average
Average     = Total_Marks / 5

#Calculating the Percentage
Percentage  = (Total_Marks/500) * 100

#Printing the Results to the User
print("Congrats "+ Name)
print(" Your Average Marks is "+ str(Average))
print(" You have Got Percentage of "+ str(Percentage) + " % out of 500")

#----------------------------Program 2-----------------------------------------------
# Make a program to take two user input & swap them


#Taking two inputs from user & Converting into integer by using int()
Number_One = int(input("Please Enter Number One : "))
Number_Two = int(input("Please Enter Number Two : "))

#printing Before Swapping of Two Numbers
print("Before Swapping",Number_One,Number_Two)

#Swapping them by using a temp variable
temp_variable = Number_One
Number_One    = Number_Two	
Number_Two    = temp_variable

#printing After Swapping of Two Numbers
print("After Swapping",Number_One,Number_Two)

#----------------------------Program 3-----------------------------------------------
# Make a program that takes a user input and test if it is Even or Odd

#Asking user to enter a number
Number    = int(input("Please Enter Number : "))

#Checking if given number is even or odd 

# if number is divisible by 2 & remainder is zero then even
if Number % 2 == 0:
    print("Even Number")
# if number is divisible by 2 & remainder is not zero then odd 
else:
    print("Odd Number")

