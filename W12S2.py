class Item:
    
    def __init__(self, category, price, rating):
        self.category = category
        self.price = price
        self.rating = rating

    def __str__(self):
        return f'Category: {self.category}, Price: ${self.price:.2f}, Rating: {self.rating}'


def print_menu():

    print('COMMAND MENU')
    print()
    print('A - Add item')
    print('D - Delete item')
    print('P - Print menu')
    print('F - Filter')
    print()

def add_item(inventory):

    name = input('Enter item name ==> ')
    category = input('Enter item category ==> ')
    price = float(input('Enter item price ==> '))
    rating = int(input('Enter item rating (1-5) ==> '))

    name = Item(category, price, rating)

    inventory.append(name)

def delete_item(inventory):

    name = input('Enter item name to delete ==> ')

    for item in inventory:
        if item.name() == name:
            inventory.remove(item)

def print_items(inventory):

    for item in inventory:
        print(item.__str__())

def filter_items(inventory):

    filterBy = input('What would you like to filter items by (category, price, rating)?')

    if filterBy.lower() == "category":

        category = input('Enter a category ==> ')
        for item in inventory:
            if item.category == category:
                print(item.__str__())
                
    elif filterBy.lower() == "price":

        price = float(input('Enter a price ==> '))
        for item in inventory:
            if item.price <= price:
                print(item.__str__())

    elif filterBy.lower == "rating":

        rating = int(input('Enter a rating ==> '))
        for item in inventory:
            if item.rating >= rating:
                print(item.__str__())

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

            
            

            

        

        

        

    
