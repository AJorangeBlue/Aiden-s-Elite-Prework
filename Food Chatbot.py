def welcome_Page():
    print("Welcome to Reon Restaurant!\nBefore I help you," 
          " I need you to answer a few questions:\n")
    
    name = input("Please enter your name: ")
    age =  input('Please enter your age: ')
    print(f'Hello {name}, aged {age}, Thank you for answering!')

def options():
    print('\nHere are the options you can take.')
    
    print(' 1. Order Food')
    print(' 2. My food hasn\'t arrived yet')
    print(' 3. Checkout')
    print(' 4. Exit Conversation')

welcome_Page()
options()

