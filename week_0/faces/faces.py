def convert(text):
    text = text.replace(":)", "🙂")
    text = text.replace(":(", "🙁")
    return text

def main():
    name = input("Enter text: ")
    result = convert(name)
    print(result)

main()        