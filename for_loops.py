

# for in range

for i in range(10):
    print("The value of i is currently", i)
    
    
for e in range(2, 8):
    print("The value of i is currently", i)
 
 
for k in range(2, 8, 3):
    print("The value of i is currently", i)



successful = True 
for number in range(3):
    print("Attempt")
    if successful:
        print("Successful!")
        break
else:
    print("Attempt 3 times and failed")
    
    
# nested loops 
    
    for x in range(5):
        for y in range(3):
            print(f"({x}, {y})")