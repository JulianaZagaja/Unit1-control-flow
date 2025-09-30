password = input("Please enter a password:")
print(f"Password : {password}")

total_chars = len(password)
letter_count = 0
digit_count = 0
uppercase_count = 0
lowercase_count = 0
special_count = 0

for char in password:
    if 'A' <= char <= 'Z' or 'a' <= char <= 'z':
        letter_count += 1
    
  
    if 'A' <= char <= 'Z':
        uppercase_count += 1
        

    if 'a' <= char <= 'z':
        lowercase_count += 1
        

    if '0' <= char <= '9':
        digit_count += 1
        
    if not ('A' <= char <= 'Z' or 'a' <= char <= 'z' or '0' <= char <= '9' or char == ' '):
        special_count += 1
     

print(f"Length: {total_chars}")
print(f"Uppercase: {uppercase_count}")
print(f"Lowercase: {lowercase_count}")
print(f"Digits: {digit_count}")
print(f"Special: {special_count}")

length = len(password)
if len(password) >= 8:
    print("Length (8+): PASSED")
else:
    print("Length (8+): Need more characters!")
    
if uppercase_count >= 1:
    print("Uppercase letters: PASSED")
else:
    print("Uppercase letters: needs an uppercase letter!")
    
if lowercase_count >= 1:
    print("Lowercase letters: PASSED")
else:
    print("Lowercase letters: needs an lowercase letter!")
    
if digit_count >= 1:
    print("Digits: PASSED")
else:
    print("Digits: needs a digit!")
    
if special_count >= 1:
    print("Specials: PASSED")
else:
    print("Specials: needs a special character!")
    
for i in range(len(password) - 2):
    if password[i] == password[i+1] == password[i+2]:
        print(f"repeated characters (3+): {password[i]}")
    else:
        print("No repeated characters!")
        break 
    
for i in range(len(password) - 2):
    if ord(password[i+1]) == ord(password[i]) + 1 and ord(password[i+2]) == ord(password[i]) + 2:
        print(f"Contains sequence: {password[i:i+3]}")
    else:
        print("Does not contain sequence!")
        break
    
if uppercase_count > 0 and lowercase_count > 0 and digit_count > 0 and digit_count > 0 and special_count > 0:
    print("FINAL RATING: Strong")
    
if uppercase_count > 0 and lowercase_count > 0 and digit_count > 0 and digit_count > 0:
    print("FINAL RATING: Medium")
else:
    print("FINAL RATING: Weak")
    