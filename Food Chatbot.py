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
    print('| 3. Checkout                    |')
    print('| 4. Close App.                  |')
    print("*--------------------------------*\n")

    op_choice = input('(Choose 1-4) How may I help you? ')

    if(op_choice == '1'):
        print('\n')
        #order_food()
    elif (op_choice == '2'):
        print('\n')
        #food_help()
    elif (op_choice == '3'):
        print('\n')
        #check_out()
    elif (op_choice == '4'):
        print('\n')
        close_app()
    else:
        print('\033[31mPlease choose a number between 1-4.\n\033[0m')
        options()



def close_app():
    print('Thank you for using the Deli Deliver App!')
    #print(f'Have a good day, {name} ({age})')
    exit()



#------Program starts below--------
#welcome_Page()
options()

