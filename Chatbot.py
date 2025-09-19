from os import name


def welcome():
    print('\nHello! Welcome to Chatbot (v0.1.6)')
    name = input('Please enter your name: ')
    age =  int(input('Please enter your age: '))

    print(f'Welcome {name} to the Elite 101 Chatbot! Your age is {age}.')

def menu():
    print('\nHere are the choices you can take.')
    
    print(' 1. Order Groceries')
    print(' 2. Read a short story')
    print(' 3. Rock, Paper, Scissors')
    print(' 4. Exit Conversation')

    

def choose_option():
    pick_choice = int(input("\nSo, how many I help you for today? "))
    if(pick_choice == 1):
        print('You chose number 1!\n')
        order_Groceries();
    elif(pick_choice == 2):
        print('You chose numero dos!\n')
        short_story();
    elif(pick_choice == 3):
        print('You chose 3, Lucky Three!')
    elif(pick_choice == 4):
        print('You have chosen # cuatro (4)!')
        exit_convers();
    else:
        print('Please choose a number between 1-4.\n')
        choose_option();

def order_Groceries():
    groceries = ['Bread', 'Apple', 'Banana', 'Chicken', 'Beef', 'Milk']
    list_of_groceries = []
    print(groceries)
    order = input("What would you like to add to the list? (Enter \'s\' to stop) ")

    while(order != 's' or order != 'S'):
        if(order in groceries):
            list_of_groceries.append(order)
            print(f'{order} added to the List.')
            order = input("\nWhat else? (Enter s to stop) ")
        else:
            print('We dont have it here!')
            order = input("\nWhat else we need? (Enter \'s\' to stop) ")
        
        if(order == 's' or order == 'S'):
            break;

    print(f'\nThe items you added in the list:\n{list_of_groceries}')

def short_story():
    print('1. The Tree of Life by Gail Berry')
    print('2. Night & Rise by Aiden Jaramillo')
    print('3. O Captain! My Captain! by Walt Whitman')

    choose_story = input('Between 1-3, choose a story to read? ')

    if(choose_story == '1'):
        print('\n\tThe Tree of Life by Gail Berry')

def exit_convers():
    print(f"farewell friend!")


# -------Main Function-------

#welcome();
menu();
choose_option();