#A Simple Database
import sys, shelve

def store_person(db):
    """
    Query user for data and store it in the shelved object.
    """
    pid = input('Enter a unique ID number: ')
    person = {}
    person['name'] = input('Enter the persons name: ')
    person['age'] = input('Enter Age: ')
    person['phone'] = input('Enter Phone Number: ')

    db[pid] = person
    return

def lookup_person(db):
    """
    Query user for ID and desired field, and fetch the corrsponding data from
    the shelf object
    """
    pid = input('enter ID Number: ')
    field = input('what would you like to know (Name, Age, Phone): ')
    field = field.strip().lower()
    print(field.capitalize() + ':' +db[pid][field])

def print_help():
    print('The available commands are:')
    print('store : Stores information about a person')
    print('lookup : Looks up a person from ID number')
    print('quit : Save changes and exit')
    print('? : Prints this message')

def enter_command():
    cmd = input('Enter Command (? for help or "quit" to exit): ')
    cmd = cmd.strip().lower()
    return cmd

def main():
    database = shelve.open('C:\\Users\\Rowan\\Documents\\GitHub\\Python\\NoviceToPro-Refresher\\DatabaseExample\\database.dat')
    try:
        while True:
            cmd = enter_command()
            if cmd == 'store':
                store_person(database)
            elif cmd == 'lookup':
                lookup_person(database)
            elif cmd == '?':
                print_help()
            elif cmd == 'quit':
                return
    finally:
        database.close()

if __name__ == '__main__': main()
