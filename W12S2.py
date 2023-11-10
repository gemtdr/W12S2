class Item:
    
    def __init__(self, category, price, rating):

    def __str__(self):
    


def print_menu():

    print('COMMAND MENU')
    print()
    print('A - Add item')
    print('D - Delete item')
    print('P - Print menu')
    print('F - Filter')
    print()

def add_item(inventory):


def delete_item(inventory):


def print_items(inventory):


def filter_items(inventory):

    filterBy = input('What would you like to filter items by (category, price, rating)?')

    if filterBy.lower() == "category":

        category = input('Enter a category ==> ')
        for item in inventory:
            if item.category == category:
                print(item.__str__())
                
    elif filterBy.lower() == "price":


    elif filterBy.lower() == "rating":

    
    else:

        print('Invalid command.')
                      

            
        

    
if __name__ == "__main__":

    again = 'y'

    inventory = []

    while again.lower() != 'n':

        print_menu()
        command = input('Type your command (A, D, P, F) ==> ')

        if command.upper() == 'A':
            add_item(inventory)

        elif command.upper() == 'D':
            delete_item(inventory)

        elif command.upper() == 'P':
            print_items(inventory)

        elif command.upper() == 'F':
            filter_items(inventory)

        else:

            continue

        again = input('Would you like to keep running this program? (Y/N) ==> ')

            
            

            

        

        

        

    
