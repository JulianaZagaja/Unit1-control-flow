#break statement in loops
#break - exit the loop immediately
#use cases:

'''
*Stop when you find something
*Exit early based on condition
*Get out of infinite loops
'''

count = 1
while count <= 10:
    print(count)
    if count == 5:
        break
    count += 1
    
while True:
    choice = input("Enter something: (q for quit):")
    if choice == "q":
        print("You wanted to exit!")
        break
    print(f"You entered {choice}")
    

n = int(input("Enter a number:"))
divisor = 2 #find first divisor

while divisor < n:
    if n % divisor == 0:
        break #Found it!
    divisor += 1

print(f"{n} is divisible by {divisor}!")


