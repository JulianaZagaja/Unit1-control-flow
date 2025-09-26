#string indexing and slicing

word = "Python"
#       012345 (positive indexing)

word[0] #P first character
word[1] #y second character
word[5] #n  last character
word[-1] #n last character
word[len(word)-1] #last character
len(word) #length of string

#string slicing

word[0:3] #pyt (characters 0,1,2)
word[:3] #pyt (characters 0,1,2)
word[2:5] #tho (characters 2,3,4)
word[2:6] #thon (characters 2,3,4,5)
word[2:len(word)] #thon (characters 2,3,4,5)
word[2:] #thon (characters 2,3,4,5)
word[-3:] #hon (characters -3,-2,-1 or 3,4,5)

# part 1 - string iteration patterns

word = "hello"

for char in word:
    print(char)
    
#index based iteration
for i in range(len(word)):
    print(f"Character {i+1}: {word[i]}")
    
char = input("Press a key:")
#character classification
#char = 'A'
#check character types using ASCII ranges
if 'A' <= char <= 'Z' or 'a' <= char <= 'z':
    print(f"'{char}' is a letter")
if 'A' <= char <= 'Z':
    print(f"'{char}' is an uppercase letter")
if 'a' <= char <= 'z':
    print(f"'{char}' is a lowercase letter")
if '0' <= char <= '9':
    print(f"'{char}' is a digit")
