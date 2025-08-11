def main():
    text = input("Input: ")
    result = shorten(text)
    print(f"Output: {result}")

def shorten(word):
    vowels = "aeiouAEIOU"
    result = ""
    for char in word:
        if (char not in vowels):
            result += char
    return result
       
     
if __name__ == "__main__":
    main()
    
