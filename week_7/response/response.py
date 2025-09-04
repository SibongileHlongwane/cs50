import validators

def main():
    email_address = input("Whats your email address? ")
    
    if validators.email(email_address):
        print("Valid")
    else:
        print("Invalid")
        
if __name__ == "__main__":
    main()
