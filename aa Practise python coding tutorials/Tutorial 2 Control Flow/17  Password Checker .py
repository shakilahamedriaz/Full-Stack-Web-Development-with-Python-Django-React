attemp = 1
key = "python123"

while attemp > 0:


    password = input("Enter correct password: ")
    if password == key:
        print(f"Access granted! 🎉 with {attemp}th attemp")
    else:
        print("Access denied! 🔒")
        print(f"Remaining time: {3 - attemp}")
    attemp += 1

    if attemp == 4:
        break
  
#