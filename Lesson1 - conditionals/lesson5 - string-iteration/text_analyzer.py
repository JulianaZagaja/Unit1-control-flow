text = input("Enter a text:")
#initialize counters
total_chars = len(text)
letter_count = 0
digit_count = 0
uppercase_count = 0
lowercase_count = 0

#track first and last character:
first_letter = None
last_letter = None

print(f"Analyzing: '{text}")
print("=" * 40)

#Process each character
for char in text:
    if 'A' <= char <= 'Z' or 'a' <= char <= 'z':
        letter_count += 1
        if first_letter is None:
            first_letter = char
        last_letter = char #keep updating (last one wins)
    #Count uppercase
    if 'A' <= char <= 'Z':
        uppercase_count += 1
        
    #Count lowercase
    if 'a' <= char <= 'z':
        lowercase_count += 1
        
    #Count digit
    if '0' <= char <= '9':
        digit_count += 1
        
    #Display the results
    print(f"Total characters: {total_chars}")
    print(f"Total letters: {letter_count}")
    print(f"Total digits: {digit_count}")
    print(f"Uppercase count: {uppercase_count}")
    print(f"Lowercase count: {lowercase_count}")
    print(f"First letter: {first_letter}")
    print(f"Last letter = {last_letter}")

