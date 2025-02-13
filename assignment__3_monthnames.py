# -*- coding: utf-8 -*-
"""Assignment _3 MonthNames.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/14TpM7dN-OT_POYHHAHIWPVOhUnXWtpls
"""

months = ["January",
"February",
"March",
"April",
"May",
"June",
"July",
"August",
"September",
"October",
"November",
"December"]
month_number = int(input("Enter the month (1-12): "))
if 1 <= month_number <= 12:
  print(f"Month {month_number} is {months[month_number - 1]}.")
else:
    print("Invalid month number. Please enter a number between 1 and 12.")

"""A certain cinema currently sells tickets for a full price of 6 pounds, but always sells tickets for half price to people who are less than 16 years old, and for a third of the price for people who are 60 years old or more.
An example run of the program (numbers in bold are typed in by the user)
Enter your age: 63
Your ticket costs £2.00

"""

def calculate_ticket_price(age):
  if age < 16:
    return 6/2
  elif age >= 60:
    return 6/3
  else:
    return 6
if __name__ == "__main__":
  try:
    age = int(input("your age: "))
    ticket_price = calculate_ticket_price(age)
    print(f"Your ticket costs £{ticket_price:.2f}")
  except ValueError:
    print("Invalid input")

"""Write a program to calculate your BMI and give weight status. Body Mass Index (BMI) is an internationally used measurement to check if you are a healthy weight for your height.The metric BMI formula accepts weight in kilograms and height in meters:

BMI= weight(kg)/height2(m2)
"""

def calculate_bmi(weight, height):
  return weight / (height * height)

def get_weight_status(bmi):
      if bmi < 18.5:
        return "Underweight"
      elif bmi < 25:
        return "Normal"
      elif bmi < 30:
        return "Overweight"
      else:
        return "Obese"
weight = float(input("your weight in (kg): "))
height = float(input("your height in (m): "))
bmi = calculate_bmi(weight, height)
weight_status = get_weight_status(bmi)
print(f"Your BMI is: {bmi:.2f}")
print(f"You are in the “{weight_status}” range.")

"""Write a Python program to receive 3 numbers from the user and print the greatest among them."""

def find_greatest(num1, num2, num3):
  if num1 >= num2 and num1 >= num3:
    return num1
  elif num2 >= num1 and num2 >= num3:
    return num2
  else:
    return num3
num1 = float(input("first number: "))
num2 = float(input("second number: "))
num3 = float(input("third number: "))
greatest_number = find_greatest(num1, num2, num3)
print(f"greatest number: {greatest_number}")

"""Find the factorial of a given number using loops(note the number is received from the user)

"""

def factorial(n):
  if n == 0:
    return 1
  else:
    factorial = 1
    for i in range(1, n + 1):
      factorial *= i
    return factorial
num = int(input("Enter a integer: "))
result = factorial(num)
print("The factorial of", num, "is", result)

"""Reverse a number using while loop"""

def reverse_number(num):
  reversed_num = 0
  while num > 0:
    digit = num % 10
    reversed_num = reversed_num * 10 + digit
    num //= 10
  return reversed_num
  num = int(input("number: "))
  reversed_num = reverse_number(num)
  print("The reversed number is:", reversed_num)

"""Finding the multiples of a number using loop

"""

def find_multiples(number, limit):
  multiples = []
  for i in range(1, limit + 1):
    multiple = number * i
    if multiple <= limit:
      multiples.append(multiple)
  return multiples
number = int(input("Enter a number: "))
limit = int(input("Enter the limit: "))
multiples_list = find_multiples(number, limit)
print("Multiples of", number, "within the limit", limit, "are:", multiples_list)

"""Write a program to print the inputted value as it is and break the loop if the value is 'done'.

"""

while True:
  user_input = input(":")
  if user_input == 'done':
    print("Done")
    break
  else:
    print(user_input)

"""Write a program that prints the numbers from 1 to 10. But for multiples of three print "Fizz" instead of the number and for the multiple of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz"



"""

for i in range(1, 10):
  if i % 3 == 0 and i % 5 == 0:
    print("FizzBuzz")
  elif i % 3 == 0:
    print("Fizz")
  elif i % 5 == 0:
    print("Buzz")
  else:
    print(i)

"""Write a program to print the following pattern:

5 4 3 2 1
4 3 2 1
3 2 1
2 1
1


"""

for i in range(5, 0, -1):
  for j in range(i, 0, -1):
    print(j, end=" ")
  print()