# if = Do some code only I some condition is true
#               else do something else

print("Please comfirm your age before signing in.")
age = int(input("I demand you to enter your age: "))


if age  >= 100:
    print("You are damn too old to sign up you dinosaur!")

elif age >= 18:
    print("You are signed in!")

elif age < 0:
    print("How an unborn possum like you are tying to sign in?")

else:
    print("You need to be older than 18 to sign in!")


# Read two numbers
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
 
# Choose the larger number
if number1 > number2:
    larger_number = number1
else:
    larger_number = number2
 
# Print the result
print("The larger number is:", larger_number)
 
 
#  # Read three numbers
# number1 = int(input("Enter the first number: "))
# number2 = int(input("Enter the second number: "))
# number3 = int(input("Enter the third number: "))
 
# # We temporarily assume that the first number
# # is the largest one.
# # We will verify this soon.
# largest_number = number1
 
# # We check if the second number is larger than the current largest_number
# # and update the largest_number if needed.
# if number2 > largest_number:
#     largest_number = number2
 
# # We check if the third number is larger than the current largest_number
# # and update the largest_number if needed.
# if number3 > largest_number:
#     largest_number = number3
 
# # Print the result
# print("The largest number is:", largest_number)
 
 
 # Other way to do it could be with this different logic:
 # Read three numbers.
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
number3 = int(input("Enter the third number: "))
 
# Check which one of the numbers is the greatest
# and pass it to the largest_number variable.
 
largest_number = max(number1, number2, number3)
 
# Print the result.
print("The largest number is:", largest_number)
 