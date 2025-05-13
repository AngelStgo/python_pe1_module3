# if = Do some code only I some condition is true
#               else do something else

print("Please comfirm your age before signing in.")
age = int(input("Enter your age"))


if age  >= 100:
    print("You are damn too old to sign up you dinosaur!")

elif age >= 18:
    print("You are signed in!")

elif age < 0:
    print("How an unborn possum like you are tying to sign in?")

else:
    print("You need to be older than 18 to sign in!")
