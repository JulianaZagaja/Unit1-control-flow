usrage = input("Enter your age:")
# rating = input("Input movie rating:")

# canwatchr = usrage >= 17
# canwatchg = usrage
# canwatchpg13 = usrage >= 13
# canwatchpg = usrage >= 6
if usrage:
    age = int(usrage)
    
rating = input("please input a movie rating:")

if age >= 17 and rating == "R":
    print("Approved, you can watch this movie!")
