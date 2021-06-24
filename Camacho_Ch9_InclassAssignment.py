
LOOK_UP = 2
ADD = 3
CHANGE = 4
DELETE = 5
QUIT = 6
DISPLAY = 1

import pickle
import pprint


def main():

    
   
    names = {}

  
    choice = 0

    while choice != QUIT:
       
        choice = get_menu_choice()

        
        if choice == LOOK_UP:
            look_up(names)
        elif choice == ADD:
            add(names)
        elif choice == CHANGE:
            change(names)
        elif choice == DELETE:
            delete(names)
        elif choice == DISPLAY:
            display(names)

    outfile = open('phonebook.txt', 'wb')
    pickle.dump(names, outfile)
    outfile.close

 


def get_menu_choice():
    print()
    print('Names in Phonebook')
    print('---------------------------')
    print('1. Display Phonebook')
    print('2. Look up a name')
    print('3. Add a new name')
    print('4. Change a name')
    print('5. Delete a name')
    print('6. Quit the program')
    print()

    
    choice = int(input('Enter your choice: '))

    while choice < DISPLAY or choice > QUIT:
        choice = int(input('Enter a valid choice: '))

    return choice

def look_up(names):
    name = input('Enter a name: ')

    print(names.get(name, 'Not found.'))


def add(names):
  
    name = input('Enter a name: ')
    pho_num = input('Enter a phone number: ')

  
    if name not in names:
        names[name] = pho_num
    else:
        print('That entry already exists.')


def change(names):
    name = input('Enter a name: ')

    if name in names:
        pho_num = input('Enter the new phone number: ')

        names[name] = pho_num
    else:
        print('That name is not found.')

def delete(names):
    name = input('Enter a name: ')

    if name in names:
        del names[name]
    else:
        print('That name is not found.')

def display(names):
    
    
    for key in names:
        
        my_file = open('phonebook.txt', 'rb')

        names = pickle.load(my_file)

        print(names)
       

        my_file.close()
   

main()

    
