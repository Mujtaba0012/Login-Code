coreect_username = "user"
correct_password = "password"

#Allow three attempts

for attempt in range(1, 4):

 print(f"Attempt {attempt}/3")

 #Input username and password

 username = input("Enter username:")
 password = input("Enter password:")

 if username == coreect_username and password == correct_password:
  print("Login successful")
  break
 
 else:
  print("invaild password")

  # if this was the last attempt, block the user

  if attempt == 3:
   print ("Too many failed attempts.Access blocked!")