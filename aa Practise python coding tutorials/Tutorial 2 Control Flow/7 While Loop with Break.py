# Guess the number game:
secret_number = 7
attempts = 0

while True:
    Guess = int(input("Guess the number (1-10): "))
    attempts += 1

    if Guess == secret_number:
        print(f"You got it in {attempts} tires!")
        break
    
    elif Guess > secret_number:
        print("Too high! Try again!")
    else:
        print("Too low! Try agian!")
   