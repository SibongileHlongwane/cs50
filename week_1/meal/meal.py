def main():
    user_input = convert(input("What time is it? "))
    if user_input <= 8 and user_input >= 7:
        print("breakfast time")
    elif user_input >= 12 and user_input <= 13:
        print("lunch time")
    elif user_input >= 18 and user_input <= 19:
        print("dinner time")
    else:
        print("")
    

def convert(time):
    hours, minutes = time.split(":")
    return int(hours) + int(minutes) / 60.0


if __name__ == "__main__":
    main()