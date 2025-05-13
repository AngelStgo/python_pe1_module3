#  LAB   Comparison operators and conditional execution
# pelargonium , Spathiphyllum, spathiphyllum

print("Guess which flower is my favorite:")
print("pelargonium, Spathiphyllum, spathiphyllum, or perhaps another one?")
print("")

# Read the flower name
name = input("Enter flower name: ")

if name == "Spathiphyllum":
    print("Yes - Spathiphyllum is the best plant ever!")
elif name == "spathiphyllum":
    print("No, I want a big Spathiphyllum!")
elif name == "pelargonium":
    print("Spathiphyllum! Not pelargonium!")
else:
    print("Spathiphyllum! Not", name + "!")
	