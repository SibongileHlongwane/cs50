def main():
    
    text = str(input("Enter statement: "))
    print(replace_space(text))
    
def replace_space(text):
    new_text = text.replace(" ", "...")
    return new_text

main()