from os import name
import random

def welcome():
    print('\nHello! Welcome to Chatbot (v1.0.1)');
    global name, age; #Admitly asked ai how name and age variable get acess global
    name = input('Please enter your name: ');
    age =  int(input('Please enter your age: ')) ;   

    print(f'Welcome {name} to the Elite 101 Chatbot! Your age is {age}.');

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
        print('\n')
        exit_convers();
    else:
        print('Please choose a number between 1-4.\n')
        choose_option();

def order_Groceries():
    groceries = ['Bread', 'Apple', 'Banana', 'Chicken', 'Beef', 'Milk']
    list_of_groceries = []
    print(groceries)
    order = input("What would you like to add to the list? (Enter \'s\' to stop) ").capitalize()

    while(order != 's' or order != 'S'):
        if(order in groceries):
            list_of_groceries.append(order)
            print(f'{order} added to the List.')
            order = input("\nWhat else? (Enter s to stop) ").capitalize()
        else:
            print('We dont have it here!')
            order = input("\nSo what can order? (Enter \'s\' to stop) ").capitalize()
        
        if(order == 's' or order == 'S'):
            break;

    print(f'\nThe items you added in the list:\n{list_of_groceries}\n')
    back_or_out();

def short_story():
    print('\tStories')
    print('1. The Tree of Life by Gail Berry')
    print('2. Night & Rise by Aiden Jaramillo')
    print('3. O Captain! My Captain! by Walt Whitman\n')

    choose_story = input('Between 1-3, choose a story to read? ')

    if(choose_story == '1'):
        print('------------------------------')
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
        print('------------------------------\n')
    
    elif(choose_story == '2'):
        print('------------------------------')
        print('\n\tNight & Rise by Aiden Jaramillo')

        print('\nEvery passing hour of the day, the bright shining sun loses its light')
        print('until the cold and dimly lit moon rises to the top.\n')

        print('As I walked inside my small, rectangular room, I slumped into my soft, comfortable bed,')
        print('having all energy depleted from my body after a long hard day of work.')
        print('I drop my eyes closed and the breathing from my nose begins slows down.\n')

        print('Time speeds by as my breathing goes to a snore, noise increases from')
        print('soft to blare, shifting positions from left to right, right to left.\n')

        print('As the moon settles down and the sun rise back up, I wake up from its big, bright')
        print('and yellow light, feeling energized again.')
        print('I got out of my bed, stretching my body, and walked out of my room,')
        print('feeling prepared to take on another challenge of the day.\n')
        print('------------------------------\n')
    
    elif(choose_story == '3'):
        print('------------------------------')
        print('\n\tO Captain! My Captain! by Walt Whitman')

        print('\nO Captain! my Captain! our fearful trip is done,')
        print('The ship has weather\'d every rack, the prize we sought is won,')
        print('The port is near, the bells I hear, the people all exulting,')
        print('While follow eyes the steady keel, the vessel grim and daring;')
    
        print('\n\tBut O heart! heart! heart!')
        print('\t O the bleeding drops of red,')
        print('\t  Where on the deck my Captain lies,')
        print('\t   Fallen cold and dead.')

        print('\nO Captain! my Captain! rise up and hear the bells;')
        print('Rise up—for you the flag is flung—for you the bugle trills,')
        print('For you bouquets and ribbon\'d wreaths—for you the shores a-crowding,')
        print('For you they call, the swaying mass, their eager faces turning;')

        print('\n\tHere Captain! dear father!')
        print('\t This arm beneath your head!')
        print('\t  It is some dream that on the deck,')
        print('\t   You\'ve fallen cold and dead.')

        print('\nMy Captain does not answer, his lips are pale and still,')
        print('My father does not feel my arm, he has no pulse nor will,')
        print('The ship is anchor\'d safe and sound, its voyage closed and done,')
        print('From fearful trip the victor ship comes in with object won;')

        print('\n\tExult O shores, and ring O bells!')
        print('\t But I with mournful tread,')
        print('\t  Walk the deck my Captain lies,')
        print('\t   Fallen cold and dead.\n')
        print('------------------------------\n')

    else:
        print('\nThat\'s not one of the three stories! Try Again.')
        short_story();

    back_or_out();

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
    
    back_or_out();

def back_or_out():
    user_command = input('Do you want to go back to the main \'menu\' or do you want to \'exit\' Chatbot? ').lower()

    if(user_command == 'menu'):
        print('Heading to main menu...');
        menu();
        choose_option();
    
    elif(user_command == 'exit'):
        print('\n');
        exit_convers();
    else:
        print('That is not a command.')
        back_or_out()



def exit_convers():
    print('Thanks for using Chatbot! I apperciate it!')
    print(f"Farewell {name}!")
    exit()


# -------Main Function-------

def main_function():
    welcome();
    menu();
    choose_option();

main_function();