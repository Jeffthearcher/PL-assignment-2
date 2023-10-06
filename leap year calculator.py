
''' KIMANI GEOFFREY CHEGE


    SCT211-0002/2019


'''
  # This program allows a user to enter any year and then determines whether the year is leap or not

  # salutes the user

name = str(input("Hello: "  "")) 

#prompts the user to enter the year

year=int(input("Please enter the year"))

# A leap year is divisible by 4 and if its divisible by 100, should also be divisible by 400
  
#tests for the leap year

if year%4==0 or (year%100==0 and year%400==0):  

    print("The Year" +"  "+ "  " + str(year) + "  " "is a leap year" ) 

else :

    print("The Year" +"  "+ "  " + str(year) + "  " "is not leap year" ) 

    
     
    



    
 



    
 