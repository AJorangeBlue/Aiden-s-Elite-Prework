def welcome():
    print('\nHello! Welcome to Chatbot (v0.1)')
    name = input('Please enter your name: ')
    age =  int(input('Please enter your age: '))

    print(f'Welcome {name} to the Elite 101 Chatbot! Your age is {age}.')

def menu():
    print('\nHere are the choices you can take.')
    
    print(' 1. Order Groceries')
    print(' 2. Read a short story')
    print(' 3. Order Food')
    print(' 4. Exit Conversation')

    pick_Choice = int(input("\nSo, how many I help you for today? "))


welcome();
menu();