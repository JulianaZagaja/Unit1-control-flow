#3 forms of range() function
#range(stop)
for i in range(5): #0,1,2,3,4
    print(i)
    
#2 range(start, stop) #3,4,5,6,7
for i in range(3,8):
    print(i)
    
#3 range(start, stop, step)
for i in range(2,11,2): #2,4,6,8,10
    print(i)

#counting backwards
for  i in range(10, 1, -2): #10,8,6,4,2
    print(i)
    
#countdown timer
import time
for i in range(10, -1, -1):
    print(f"Seconds: {i}")
    #time.sleep(1) wait 1 second between numbers
    if i == 0:
        print("Blast off! 🚀")

#multiplication table
#take user input for the number and print the table
# number x 1 = number
#if the user submitted 5
#5x1=5
#5x2=10

#my way
num = int(input("Enter a number (1-12):"))

for i in range(1, 13):
    print(f"{num} x {i:2d} = {(num*i):3d}")
    
#his way
num = int(input("Enter a number (1-12):"))

if 1 <= num <= 12:
    for i in range(1, 13):
        result = num * i
        print(f"{num} x {i:2d} = {result:3d}")
    else:
        print("Please enter a number between 1 and 12.")
