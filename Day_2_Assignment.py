"""Author    : Shaik Salman Khan
   CreatedOn : Oct 22/2020
   Purpose   : Submitting Day_2 Programming assignment 	
"""

#----------------------------Program 1------------------------------------
# Make a program to input three numbers  & print the highest

#Asking user to enter three numbers
Number_1 = int(input("Please enter number one   : "))
Number_2 = int(input("Please enter number two   : "))
Number_3 = int(input("Please enter number three : "))

#If Users enters two or three same numbers 
if Number_1 == Number_2 or Number_2 == Number_3 or Number_3 == Number_1:
      if Number_1 == Number_2 == Number_3:
           print("Sorry We can't find Highest Bcuz You have Entered three Same Numbers")
      else:
           print("Sorry we can't find Highest Bcuz You have Entered Two Same Numbers") 

#If User Enters three Different Number
else:
    #Checking the highest Number
    if   Number_1 > Number_2 and Number_1 > Number_3:
          print("Number One is Highest ")
    elif Number_2 > Number_1 and Number_2 > Number_3:
          print("Number Two is Highest ")
    else:
          print("Number Three is Highest")

#----------------------------Program 2------------------------------------
# Make a program to input number  & print the Table of it

#Asking user to enter number
Number = int(input("Please enter number :"))

#Printing the Table of Given Number
for i in range(1,11):
    #Printing like 5 * 1 = 5
    print(Number," * ",i," = ",Number * i)

#----------------------------Program 3------------------------------------
# Make a program to input 10 number and get sum of all

#For counting the Sum
Count = 0

#Using a For Loop to Take Ten inputs
for i in range(1,11):
    #Asking user to enter number
    Number = int(input("Please enter number :"))
    Count  = Count + Number
    
#Printing the Sum of 10 inputs
print("The Sum of 10 Inputs are :",Count)    

#----------------------------Program 4------------------------------------
# Create a Function that return sum of two numbers if number are >= 10

#Creating a func that takes two parameters i.e; Number_1 & Number_2
def Sum_of_TwoNumbers(Number_1,Number_2):
    #Checking if numbers are greater than 10
    if Number_1 >= 10 and Number_2 >= 10:
        Sum = Number_1 + Number_1
        return Sum
    #Checking if numbers are lesser than 10
    else:
        #if Both Numbers are same
        if Number_1 ==  Number_2: 
            print("Sorry we cant Find Sum bcuz your both numbers are lesser than 10")
        #if Both Numbers are Different
        else:
            print("Sorry we cant Find Sum bcuz your one numbers is lesser than 10")

#Calling the Function
Output = Sum_of_TwoNumbers(11,12)
print(Output)        

#----------------------------Program 5------------------------------------
# Create a Function that accepts a name and return the reverse of it

#Creating a func that takes name parameter
def Reverse_Name(Name):
    #Getting the Length of given string by using len() func 
    Length   =  len(Name)- 1

    #Using a reverse variable to store the reverse string 
    reverse  =  ""

    #Using a for loop to reverse the string 
    for i in range(Length,-1,-1):
         reverse = reverse + Name[i]
    return reverse

    
#Calling the Function
Output = Reverse_Name("Salman")
print(Output)        
