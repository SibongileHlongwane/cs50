
while True:
    try:
        user_input = input("Fraction: ").strip()
        x, y = user_input.split("/")
        x = int(x)
        y = int(y)
            
        if y == 0:
            raise ZeroDivisionError
        if x > y or x < 0:
            raise ValueError
                
        percentage = round((x / y) * 100)
                
        if percentage <= 1:
            print("E")
        elif percentage >= 99:
            print("F")
        else:
            print(f"{percentage}%")
        break    
        
    except (ValueError, ZeroDivisionError):
        print("Invalid input")
        
    
