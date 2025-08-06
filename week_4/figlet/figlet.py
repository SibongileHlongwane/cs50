from pyfiglet import Figlet
import random
import sys

figlet = Figlet()
available_fonts = figlet.getFonts()

    
def do_figlet(): 

    if len(sys.argv) == 1:
            random_font = random.choice(available_fonts)
            gather_text_and_print(random_font)
            
    elif len(sys.argv) == 3 and sys.argv[1] == "-f":
        font_from_arg = sys.argv[2]
        if font_from_arg not in available_fonts:
            print_invalid_usage_and_exit()
        gather_text_and_print(font_from_arg)
        
    else:
        print_invalid_usage_and_exit()
               
def gather_text_and_print(font_to_use):
    figlet.setFont(font=font_to_use)
    word = input("Input: ")
    print(figlet.renderText(word))
    
def print_invalid_usage_and_exit():
    print("Invalid usage")
    sys.exit(1)
        
if __name__ == "__main__":
    do_figlet()




