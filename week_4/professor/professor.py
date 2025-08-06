from random import randint


def main():
    level = get_level()
    correct = 0
    for _ in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        counter = 0
        while counter < 3:
            try:
                ans = int(input(f"{x} + {y}="))
                if ans == (x+y):
                    correct += 1
                    break
                else:
                    print("EEE")
                    counter += 1
            except ValueError:
                print("EEE")
                counter += 1    
        if counter == 3:
            print(f"{x}+{y}={x+y}")
    print(f"Score: {correct}")

def get_level():
    while True:
        level = input("Level: ")
        if not level.isdigit(): 
            continue
        level = int(level)
        if level in [1, 2, 3]:  
            return level


def generate_integer(level):
    if level == 1:
        return randint(0,9)
    elif level == 2:
        return randint(10,99)
    elif level == 3:
        return randint(100,999)
        


if __name__ == "__main__":
    main()