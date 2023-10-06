''' KIMANI GEOFFREY CHEGE

    SCT211-0002/2019

'''
# A bill calculator program

# prompts the user to enter the total bill, tip percentage and the number of people

total_bill=float(input("The total Bill is :"))

tip_percentage=int(input("What percentage would you like to tip me?"))

'''n is the no of people'''

n=int(input("How many are you?"))
total_amount =float(tip_percentage/100*total_bill+total_bill)

#computes the bill per person 'B'

B=float(total_amount/n)
 
D=(round(B,2))
#prints the bill per person formatted to decimal points


print("The total bill per person is: " + str(D)  )