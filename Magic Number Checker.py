# Magic Number Checker

magic_number = 7

number = int(input("Guess the magic number (1-10): "))

if number == magic_number:
    print("Congratulations! You guessed the magic number.")
else:
    print("Wrong Guess! Try Again.")