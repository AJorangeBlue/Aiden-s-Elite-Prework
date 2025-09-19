from os import name
import random

def welcome():
    print('\nHello! Welcome to Chatbot (v0.7.8)')
    global name, age #Admitly asked ai how name and age variable get acess global
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
        print('\n')
        order_Groceries();
    elif(pick_choice == 2):
        print('\n')
        short_story();
    elif(pick_choice == 3):
        print('\n')
        play_RPS();
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
    print('\tStories')
    print('1. The Tree of Life by Gail Berry')
    print('2. Night & Rise by Aiden Jaramillo')
    print('3. O Captain! My Captain! by Walt Whitman')

    choose_story = input('Between 1-3, choose a story to read? ')

    if(choose_story == '1'):
        print('\n\tThe Tree of Life by Gail Berry')

        print('\n\"Deep within the forest is the golden tree, the Tree of Life. \n' \
        'Let your quest be for that and none other,\" the old woman advised.\n')
        print('Some seek it for its golden leaves and dreams of riches. They do not find it.\n')
        print('And some, some look for healing from its roots. \
              \nSome of those do find it, but they are few.\n')
        
        print('And then, then there are the ones who search only for the joy of the quest \
              \nand the wonder of what they might find.\n')
        print('And these, these are the ones for whom the tree of life bows her golden branches.\n')

        print('\"Be you one of these, master?\" cackled the old woman.\n')
        print('And I replied without knowing why, \"Yes, old woman, I am.\" \n')


def play_RPS():
    print('Let us play Rock, Paper and Scissors!')
    user_RPS = input('(\'R\' = rock) -- (\'P\' = Paper) -- (\'S\' = Scissors)\nWhat do you choose? ').upper()
    
    RPS_options = ['R', 'P', 'S']
    chatbot_pick = random.choice(RPS_options)
    print(f'Chatbot uses {chatbot_pick}.\n')

    if(user_RPS == chatbot_pick):
        print('It\'s a TIE!\n')
    elif((user_RPS == 'R' and chatbot_pick == 'S') or (user_RPS == 'P' and chatbot_pick == 'R')  or (user_RPS == 'S' and chatbot_pick == 'P')):
        print('You WIN!\n')
    elif((user_RPS == 'R' and chatbot_pick == 'P') or (user_RPS == 'P' and chatbot_pick == 'S')  or (user_RPS == 'S' and chatbot_pick == 'R')):
        print('You LOSE!\n')
    else:
        print('That is not one of the commands! Try Again!\n')
        play_RPS();
    




def exit_convers():
    print('\nThanks for using Chatbot! I apperciate it!')
    print(f"farewell {name}!")


# -------Main Function-------

def main_function():
    welcome();
    menu();
    choose_option();

main_function();