import random
random_number = random.randint(1, 11)
while True:
    num = int(input("Enter a number between 1 and 10: "))
    if num > random_number:
        print("Too high")
    elif num < random_number:
        print("Too low")
    else:
        print("You guessed it right the number is", random_number)
        break