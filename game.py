import random
print("--------------------------------------")
print("x                                    x")
print("      welcome to the game ....        ")
print("x                                    x")
print("--------------------------------------")
secret_num = random.randint(1,50)
attempts = 0
while True:
    guessed_num = int(input("\n*Enter your guess (1,50) : "))
    attempts += 1
    if guessed_num > secret_num:
        print("Too high...! Try again")
    elif guessed_num < secret_num:
        print("Too low...! Try again")
    else:
        print(f"congratulation !!! You guessed it right in {attempts} attempts & You won...")
        break
