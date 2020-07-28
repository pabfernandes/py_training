# This program will run a menu to list all cars
from maker_class import CarMaker

def menu():
    menu_continue = True
    while menu_continue:
        print(f"Choose your option")
        print(f"1 - add a brand")
        print(f"2 - print brands")
        print(f"3 - exit")
        chosen_option = input()
        
        if chosen_option == "1":
            brand = input(f"What is the name of the brand you want to add?\n")
            country = input(f"Which is the country of {brand}?\n")
            brand = CarMaker(brand, country)

        elif chosen_option == "2":
            for maker,country in CarMaker.all_makers.items():
                print(f"{maker.title()} is from {country.title()}")

        elif chosen_option == "3":
            menu_continue = False
        
        else:
            print(f"Please, choose a valid option")
            continue

menu()
