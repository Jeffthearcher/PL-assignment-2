''' KIMANI GEOFFREY CHEGE

    SCT211-0002/2019

'''
# This program accepts the date of birth from the user , determines his age 
# Then the output is displayed in the form of months, days and years and months

#!/usr/bin/python3


# import datetime module for birth dates;
import datetime


def simple_calc():
    '''
    this function accepts date of birth from a user
    subtracts it from the current date and outputs the age of the user
    '''

    # welcome user:
    user_name = str(input('Please enter your name: '))
    salute = f'Hello, {user_name}. Welcome to my AGE calculator :'
    print(salute)

    # prompt for date of birth input from the user:
    birth_date = datetime.datetime.strptime(input('Please enter your date of birth (YYYY-MM-DD): '), '%Y-%m-%d')

    # calculate age
    current_date = datetime.datetime.today()
    age = current_date - birth_date

    # calculate age in years, months, and days - convert to int to rm float points; 
    age_in_years = int(age.total_seconds() // (365 * 24 * 60 * 60))
    age_in_months = int((age.total_seconds() // (30 * 24 * 60 * 60)) % 12)
    age_in_days = int(age.days % 30)

    # print age
    print()
    print(f'Your AGE is {age_in_years} years, {age_in_months} months, and {age_in_days} days.')


simple_calc()