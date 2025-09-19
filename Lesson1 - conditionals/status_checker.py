# Student Information System - Starter Code

print("STUDENT INFORMATION SYSTEM")
print("========================================")

# Get student information
name = input("Enter student name: ")
age = int(input("Enter student age: "))
gpa = float(input("Enter student GPA (0.0-4.0): "))

# Show student information
print()
print("Student Information:")
print("Name:", name)
print("Age:", age)
print("GPA:", gpa)
print()

# TODO: Check if age is valid (between 16 and 100)
if 16 <= age <= 100:
    print("Age is valid")
else:
    print("Age is not valid")

# TODO: Check if GPA is valid (between 0.0 and 4.0)
if 0.0 <= gpa <= 4.0:
    print("GPA is valid")
else:
    print("GPA is not valid")

# TODO: Check enrollment eligibility (age >= 18 AND gpa >= 2.0)
if age >= 18 and gpa >= 2.0:
    print("Eligible to enroll")
else:
    print("Not eligible for enrollment!")

# TODO: Check voting eligibility (age >= 18)
if age >= 18:
    print("Eligible to vote!")
else:
    print("Not old enough to vote!")

# TODO: Check honor roll status (gpa >= 3.5)

if gpa >= 3.5:
    print("Honor roll student!")
else:
    print("Not on honor roll")