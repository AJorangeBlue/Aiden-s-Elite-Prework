from os import name

def welcome_Page():
    print("Welcome to Deli Deliver App!\nBefore I help you," 
          " I need you to answer a few questions:\n")
    
    global name, age;

    name = input("Please enter your name: ")
    age = input('Please enter your age: ')


    # make a little display info and ask if it is the correct info
    print(f"\nName: {name}\nAge: {age}")
    correct_info = input("Is your info. correct? (y/n): ").strip().lower()
    while (correct_info != 'yes' and correct_info != 'y'):
        print("\nTry again and remember to enter your correct information.")
        name = input("Please enter your name: ")
        age = input('Please enter your age: ')

        print(f"\nName: {name}\nAge: {age}")
        correct_info = input("Is your info. correct? (y/n): ").strip().lower()
    
    if(age < '18'):
        print(f'\nSorry {name}, but must be at least 18 years old to use this app.')
        print('...App closing...')
        exit()

    print(f'\033[32m\nWelcome {name} ({age}) to Deli Deliver App!\n\033[0m')

    
    

def options():
    print('\033[31m\nDeli Deliver Menu\033[0m')
    
    print("*--------------------------------*")
    print('| 1. Order Food                  |')
    print('| 2. My food hasn\'t arrived yet  |')
    #print('| 3. Checkout                    |')
    print('| 3. Close App.                  |')
    print("*--------------------------------*\n")

    op_choice = input('(Choose 1-4) How may I help you? ')

    if(op_choice == '1'):
        print('\n')
        order_food()
    elif (op_choice == '2'):
        print('\n')
        #food_help()
    #elif (op_choice == '3'):
        #print('\n')
        #check_out()
    elif (op_choice == '3'):
        print('\n')
        close_app()
    else:
        print('\033[31mPlease choose a number between 1-4.\n\033[0m')
        options()


def order_food():
    food_items = ["fries", "hamburger", "cheeseburger", "tenders", "salad"]
    drink_items = ["water", "coke", "pepsi", "lemonade", "apple juice"]

    global a
    a = "-"
    
    print("\033[33mFood Menu\033[0m")
    print("*" +str(48 * a)+ "*")
    print(f'| Fries  Hamburger  Cheeseburger  tenders  Salad |')
    print(f'| Water   Coke   Pepsi   Lemonade   Apple Juice  |')
    print("*" +str(48 * a)+ "*")
    

    order = input("\nWhat would you like to order? Press s to stop.\n").lower()
    orderUP(order, food_items, drink_items)
    

    credit_cards = ["Visa", "Chase", "Mastercard", "Capital", "Wells"]
    print(credit_cards)
    pay_with = input("What do you want to pay with? ").capitalize()

    while pay_with not in credit_cards:
        print('\033[31mThat is invalid, try again!\033[0m')
        pay_with = input("What do you want to pay with? ").capitalize()
    
    print('\nCard Accepted!')
    print('Your order will arrive later today.')



def orderUP(order, food_items, drink_items):
    your_items = []
    cost = 0

    while order != 's':
        if order in food_items or order in drink_items:
            your_items.append(order)
            print(f'\033[32m{order} added!\033[0m')
            cost += 1 # Assumption of the cost
            order = input("\nWhat else? Press s to stop.\n").lower()
        else:
            print('That does not exist!')
            order = input("\nOrder Again. Press s to stop.\n").lower()
    cost += (cost * 0.15)

    print("*" +str(25 * a)+ "*")
    print(f'Here is your order: {your_items}')
    print(f'Total: ${cost}\n')


# Option 4 - Close application
def close_app():
    print('Thank you for using the Deli Deliver App!')
    #print(f'Have a good day, {name} ({age})')
    exit()




#------Program starts below--------
#welcome_Page()
options()

