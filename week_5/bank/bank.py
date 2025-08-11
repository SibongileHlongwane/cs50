def main():
    try:
        greeting = input("Greeting: ").strip()
        result = value(greeting)
        print(f"{result}")
    except EOFError:
        print("")


def value(greeting):
    greeting_lower = greeting.lower()
    if greeting_lower.startswith("hello"):
        return "$0"
    elif greeting_lower.startswith("h"):
        return "$20"
    else:
        return "$100"


if __name__ == "__main__":
    main()
    
    
    
   