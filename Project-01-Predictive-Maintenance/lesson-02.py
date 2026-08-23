# This is a simple Python program that prompts the user for their name, age, and country of residence, and then prints a greeting message using that information.
name= input("What is your name? ")
age= int(input("What is your age? "))
country= input("What country are you from? ")
print(f"hello {name},\n you are {age} years old and you live in {country}.")
# This is a pythom program that calculates the users age in 5,10 and 20 years and prints the result
age_in_5_years= age+5
age_in_10_years= age+10
age_in_20_years= age+20
print(f" in 5 years you  will be {age_in_5_years} years old.")
print(f" in 10 years you  will be {age_in_10_years} years old.")
print(f" in 20 years you will be {age_in_20_years} years old.")
# simple calculator: a program tha collects two numbers from a user and perform simple arthematic operations on them
num1= float(input("Enter the first number: "))
num2= float(input("Enter the second number: "))
sum_result=int( num1+num2)
difference=int( num1-num2)
product= int(num1*num2)
quotient= num1/num2
print(f"The sum of {num1} and {num2} is: {sum_result}")
print(f"The difference of {num1} and {num2} is: {difference}")
print(f"The product of {num1} and {num2} is: {product}")
print(f"The quotient of {num1} and {num2} is: {quotient}")
num3=int(input("Enter the third number: "))
# This is a simple Python program that checks if a number is even or odd and prints the result.
if num3%2==0:
    print(f"{num3} is an even number.")
else:
    print(f"{num3} is an odd number.")