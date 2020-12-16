import random
import os


try:
    import pyfiglet
    from colorama import init, Fore, Style
except ImportError:
     os.system("pip3 install pyfiglet")
     os.system('pip3 install colorama')

os.system("cls")

if __name__ == "__main__":
    r = Fore.RED
    g = Fore.GREEN
    b = Fore.BLUE
    y = Fore.YELLOW
    print(r + pyfiglet.figlet_format('The DiCe') + b )
    print("author: Mortal_coder\n")

    print("Hello i m the best alternate to a physical dice,")
    print(y + "let me choose a number on a dice" + g)
    while True:
        listw = list("123456")
        e = random.choice(listw)
        print(b+"outcome /",e + g) 
        a = input("if u want to roll the dice again(if u don't want to then just type " + r + "no" + g + ") just press "+ y +"enter/" +g)
        if 'no' in a:
            exit()
        else:
            pass
