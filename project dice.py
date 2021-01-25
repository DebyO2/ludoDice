import random
import os

try:
    import pyfiglet
    from colorama import init, Fore, Style
except ImportError:
     os.system("pip3 install pyfiglet")
     os.system('pip3 install colorama')

def clr():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

if __name__ == "__main__":
    r = Fore.RED
    g = Fore.GREEN
    b = Fore.BLUE
    y = Fore.YELLOW
    f = pyfiglet.Figlet(font='slant')
    logo = f.renderText('Dicey')
    print(r + logo + g)
    print("Author: Mortal_coder\n")

    print("Hello i\'m the best alternate to a physical dice,")
    print(y + "Let\'s get rollin\'!" + g)
    while True:
        listw = list("123456")
        e = random.choice(listw)
        print(f'{b}Outcome : {e}{g}') 
        a = str(input(g + 'Wanna roll me again?[y/n]: '))
        if a == 'n':
            exit()
        else:
            pass
