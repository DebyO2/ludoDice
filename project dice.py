import random
import os


try:
    import pyfiglet
    from colorama import init, Fore, Style
except ImportError:
     os.system('''
     pip install pyfiglet
     pip install colorama
     ''')

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
    rs = Fore.RESET
    clr()
    f = pyfiglet.Figlet(font='slant')
    logo = f.renderText('Dicey')
    print(r + logo + rs)
    print(g + "Author: Mortal_coder\n" + rs)

    print(g + "Hello i m the best alternate to a physical dice," + rs)
    print(y + "Here I roll!" + g)
    while True:
        listw = list("123456")
        e = random.choice(listw) #random is the freakin' module that helps u to print random numbers ;)
        print(b+"outcome /",e + g) 
        a = str(input('Wanna roll me again?[enter/n]')
        if a == 'n'
            exit()
        else:
            pass
