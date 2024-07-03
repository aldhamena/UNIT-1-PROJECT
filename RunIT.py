from Initializing import *
from colorama import *
from art import *

print(Fore.MAGENTA + "-"*100)
tprint("WELCOME","rnd-xlarge")

print('''hello there
This program is designed to help you choose the right sport
To do so we will ask you to provide some information
like your name, age, Height, and weight
we also need you to be aware of your parents' heights
which will help us expect your height in the future''')



while True:

    x = input("Are you ready to register? type (Y) for YES , (N) for NO to quit: ")
    

    if x.upper() == "Y":
        Player1 = Player()
        
        print(Player1)
        print(Fore.BLUE + "-"*100)
        print(Player1.Expected_Adult_Age_Height())
        print(Fore.GREEN + "-"*100)
        print(Player1.Player_BMI())
        print(Fore.RED + "-"*100)
        print(Player1.suggested_sports())
        print(Fore.YELLOW + "-"*100)
        print(Player1.chosen_sport())

    elif x.upper() == "N":
        print("Thank you for being here")
        break