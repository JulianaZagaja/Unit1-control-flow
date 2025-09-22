usrage = input("Enter your age:")

if usrage:
    age = int(usrage)
    
rating = input("please input a movie rating:")

if age >= 17 and rating == "R":
    print("Approved, you can watch this movie!")
else:
    print("Denied, must be 17+ for R-rated movies")

if age <= 6 and rating == "PG":
    print("approved, you can watch this movie!")
else:
    print("not of age, not reccomended!")
    
if age >= 13 and rating == "PG-13":
    print("Approved, you can watch this movie!")
else:
    print("Warning, not reccomended for your age!")
    
if age > 0 and input == "G":
    print("You can watch this movie!")