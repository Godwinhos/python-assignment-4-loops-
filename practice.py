'''
Write code that does the following:

Ask for a person's age.

If age is 18 or above:

Ask if they have a valid ID (yes or no)

If yes: print "You may enter."

If no: print "Bring your ID next time."

If under 18:

If age is 16 or 17: print "Come with an adult."

Else: print "You're too young."

Want the solution? Ask me or try it yourself
'''
'''
age = int(input("enter your age: "))
if age >= 18:
    valid_ID =input("(yes/no)").lower()
    if valid_ID == "yes":
        print("you may enter")

    else:
        print("access denied")
elif 16 <= age <17:
    print("come with an adult")
else:
    print("too young")
'''

'''
Problem 4: Login System (Nested If)
Ask user:

Username

Password

If username is “admin”:

Then check if password is “1234”

If yes → print: “Login successful.”

If no → print: “Incorrect password.”

Else → print: “Unknown user.”
'''

username = input("enter your username")
password = int(input("enter your password"))
if username == "godwino":
    if password == 1234:
        print("login successful")
    else:
        print("incorrect credentials")
else:
    print("wrong user")





