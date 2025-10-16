# while True:
#     username= input("Enter a username:")
#     if len(username) < 3:
#         print("This password is too short!")
#         continue
#     if len(username) > 15:
#         print("This password is too long!")
#         continue
    
#     has_space = False
#     for char in username:
#         if char == " ":
#             has_space = True
#             print("No spaces allowed!")
#             continue
#         break 
    
#     while True:
#         password = input("Enter a password (8+ characters):")
#         if len(password) < 8:
#             print("Password is too short")
#             continue
        
#         has_digit = False
#         has_uppercase = False
        
#         for char in password:
#             if "A" <= char <= "Z":
#                 has_uppercase = True
                
#             if "0" <= char <= "9":
#                 has_digit = True 
                
#         if not has_digit:
#             print("Requires atleast one digit")
#             continue
#         if not has_uppercase:
#             print("Requires atleast one uppercase letter!")
#             continue
#         break
    
#     while True:
#         Age = input("Please enter a page:")
#         if Age