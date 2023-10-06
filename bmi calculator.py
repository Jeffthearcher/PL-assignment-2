''' KIMANI GEOFFREY CHEGE

    SCT211-0002/2019
'''

# A BMI app that informs the user if he/she is underweight, normal weight or overweight

# The app simply greets the user and asks for his/her name
name=str(input("Please enter your name:"))

print("Hello," + "   " + name)

#prompts the user to enter the weight and height

weight=float(input("Please enter your weight"))

height=float(input("Please enter your height"))

#computes the BMI -()
BMI = weight/(height*height)

print(BMI)
# use of control structures (if statement) to determine if the user is underweight ,overweight or normal weight

if  BMI<18.5 :
        print(f"Hello" "  " + name + "   " + "you are underweight")

elif BMI<=24.9 :

        print("Good work""  " + name + "   " +  "you are of healthy weight")

elif BMI<=29.9 :

        print( name + "   " + "you have an over weight")

else :

        print("Hello " + name + "   " + "you are Obese")
        















