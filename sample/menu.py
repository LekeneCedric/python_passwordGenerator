import colorama
from colorama import Fore
import os
from core import *

def principal_menu():
    os.system('clear')
    print("|----------------------------------------------------------------------------|")
    print("|----------------------------PASSWORD GENERATOR------------------------------|")
    print("|  Simple tools to generate random password for online accounts creation     |")        
    print("|----------------------------------------------------------------------------|")
    print("|  1 - Generate simple password                                              |")
    print("|----------------------------------------------------------------------------|")
    print("|  2 - Generate custom password                                              |")
    print("|----------------------------------------------------------------------------|")
    print("|  3 - Exit                                                                  |")
    print("|----------------------------------------------------------------------------|")
    print("|----------------------------------------------------------------------------|")
    choix = int(input(">>"))
    match choix:
        case 1 :
            simple_sub_menu()
        case 2 :
            custom_sub_menu(0,None,None,None,None)
        case 3:
            print("See you soon :) ")
            exit(-1)
        case _:
            exit(-1)

def simple_sub_menu():
    lenght = 0 
    while lenght<10:
        os.system('clear')
        print("|----------------------------------------------------------------------------|")
        print("|----------------------------PASSWORD GENERATOR------------------------------|")
        print("|  Enter the lenght of your password                                         |")        
        print("|----------------------------------------------------------------------------|")
        lenght = int(input(">>"))
        result_simple_menu(generate_simple_password(lenght),lenght)
    
def custom_sub_menu(lenght,up,lo,sy,nu):
    while lenght<10 or up == None and lo == None and sy == None and nu == None:
        os.system('clear')
        print("|----------------------------------------------------------------------------|")
        print("|----------------------------PASSWORD GENERATOR------------------------------|")
        print("|  (1) The lenght of your password                                           |")
        print("|----------------------------------------------------------------------------|")
        print("|  for the following questions answer yes or no (O/N)                        |")
        print("|----------------------------------------------------------------------------|")
        print("|  (2) will it contain capital letters ? O/N                                 |")
        print("|----------------------------------------------------------------------------|")
        print("|  (3) will it contain minicules ? O/N                                       |")
        print("|----------------------------------------------------------------------------|")
        print("|  (4) will it contain symbols ? O/N                                         |")
        print("|----------------------------------------------------------------------------|")
        print("|  (5) will it contain numbers ? O/N                                         |")
        print("|----------------------------------------------------------------------------|")       
        print("|----------------------------------------------------------------------------|")
        lenght = int(input("(1) >>"))
        up = True if "o" in input("(2) >>").lower() else False
        lo = True if "o" in input("(3) >>").lower() else False
        sy = True if "o" in input("(4) >>").lower() else False
        nu = True if "o" in input("(5) >>").lower() else False
        result_custom_menu(generate_custom_password(lenght,[up,lo,sy,nu]),lenght,[up,lo,sy,nu])

def result_custom_menu(password,lenght,require):
    os.system('clear')
    print("|----------------------------------------------------------------------------|")
    print("|----------------------------PASSWORD GENERATOR------------------------------|")
    print("|  Generated password : \033[1;32m{}\u001b[37m                               ".format(password))        
    print("|----------------------------------------------------------------------------|")
    print("|  1 - Regenerate                                                            |")
    print("|----------------------------------------------------------------------------|")
    print("|  2 - Back                                                                  |")
    print("|----------------------------------------------------------------------------|")
    print("|  3 - Back To Main Menu                                                     |")
    print("|----------------------------------------------------------------------------|")
    print("|  4 - Exit                                                                  |")
    print("|----------------------------------------------------------------------------|")
    print("|----------------------------------------------------------------------------|")
    choix = int(input(">>"))
    match choix:
        case 1 :
            result_custom_menu(generate_custom_password(lenght,require),lenght,require)
        case 2 :
            custom_sub_menu(0,None,None,None,None)
        case 3:
            principal_menu()
        case 4:
            print("See you soon :) ")
            exit(-1)
        case _:
            exit(-1)
            
def result_simple_menu(password,lenght):
    os.system('clear')
    print("|----------------------------------------------------------------------------|")
    print("|----------------------------PASSWORD GENERATOR------------------------------|")
    print("|  Generated password : \033[1;32m{}\u001b[37m                               ".format(password))        
    print("|----------------------------------------------------------------------------|")
    print("|  1 - Regenerate Password                                                   |")
    print("|----------------------------------------------------------------------------|")
    print("|  2 - Regenerate with same lenght                                           |")
    print("|----------------------------------------------------------------------------|")
    print("|  3 - Back                                                                  |")
    print("|----------------------------------------------------------------------------|")
    print("|  4 - Exit                                                                  |")
    print("|----------------------------------------------------------------------------|")
    print("|----------------------------------------------------------------------------|")
    choix = int(input(">>"))
    match choix:
        case 1 :
            simple_sub_menu()
        case 2 :
          result_simple_menu(generate_simple_password(lenght),lenght)  
        case 3:
            principal_menu()
        case 4:
            print("See you soon :) ")
            exit(-1)
        case _:
            exit(-1)