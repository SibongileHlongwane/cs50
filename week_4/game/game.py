import random

while True:
    level = input("Level: ")
    if not level.isdigit() or int(level)<1:
        continue
    break

level = int(level)
x = random.randint(1 ,level)

while True:
    try:
        guess = int(input("Guess: "))
        if guess < 1:
            continue
        if guess < x:
            print("Too small!")
            continue
        if guess > x:
            print("Too large!")
            continue
        else: 
            print("Just right!")
            break
    except ValueError:
        continue
    