
from tabulate import tabulate
import pandas as pd

#========The beginning of the class==========
class Shoe:
    shoe_string = ""

    def __init__(self, country, code, product, cost, quantity):
        # pass
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity
        

        '''
        In this function, you must initialise the following attributes:
            ● country,
            ● code,
            ● product,
            ● cost, and
            ● quantity.
        '''
    def get_cost(self):
        return self.cost
        '''
        Add the code to return the cost of the shoe in this method.
        '''

    def get_quantity(self):
        return self.quantity
        '''
        Add the code to return the quantity of the shoes.
        '''

    def __str__(self):
        
        self.shoe_string = f"Country is:(country={self.country}, Code is:(code={self.code}\
                Product is:(product={self.product}, Cost is:(cost={self.cost}\
                   Quantity is:(quantity={self.quantity}) "
        return self.shoe_string
        '''
        Add a code to returns a string representation of a class.
        '''


#=============Shoe list===========
'''
The list will be used to store a list of objects of shoes.
'''
shoe_list = []
#==========Functions outside the class==============
def read_shoes_data():
    try:

        with open('T32/inventory.txt', 'r') as f:

            # read the first line and discard it
            next(f)

            # read the rest of the lines
            # lines = f.readlines()
            for line in f:
                line = line.strip().split(',')
                shoe = Shoe(line[0], line[1], line[2], line[3],line[4])
                shoe_list.append(shoe)
                # print(shoe_list)
                # line = line.Shoe()
                # line_object = shoe_list.append(line)
                # print(line_object)


    except FileNotFoundError:
        print("File not found.")
    except:
        print("An error occurred.")    

read_shoes_data()   
    # pass

'''
    This function will open the file inventory.txt
    and read the data from this file, then create a shoes object with this data
    and append this object into the shoes list. One line in this file represents
    data to create one object of shoes. You must use the try-except in this function
    for error handling. Remember to skip the first line using your code.
    '''
# def capture_shoes(self):
    
#     self.country = input("Where is the shoe made? ")
#     self.code = input("Enter shoe SKU: ")
#     self.product = input("Enter brand name: ")
#     self.cost = int(input("Enter shoe price: "))
#     self.quantity = int(input("Enter shoe quantity in Kg"))
#     self.shoe_data = self.country, self.code, self.product, self.cost, self.quantity
#     for shoe in self.shoe_data:
#         self.shoe_object = shoe_list.append(self.shoe_data)
#         print(self.shoe_object)

    # pass
'''
    This function will allow a user to capture data
    about a shoe and use this data to create a shoe object
    and append this object inside the shoe list.
    '''

def view_all():
    # pass
    for shoe in shoe_list:
        table = shoe_list
        print(shoe)
    # print(tabulate(table, shoe))
        
    '''
    This function will iterate over the shoes list and
    print the details of the shoes returned from the __str__
    function. Optional: you can organise your data in a table format
    by using Python’s tabulate module.
    '''

def re_stock():
    

    # Read in the file
    df = pd.read_csv('T32/inventory.txt', names=['country', 'code', 'product', 'cost', 'quantity'])

    # Group by country and find the object with the lowest quantity for each country
    grouped = df.groupby('country')
    for country, group in grouped:
        lowest_obj = group[group['quantity'] == group['quantity'].min()]
        print(f'In {country}, Object with lowest quantity: {lowest_obj["product"].values[0]}, Quantity: {lowest_obj["quantity"].values[0]}')

    # Allowing new products to be added 
        add_quantity = input(f'Do you want to add to the product {lowest_obj["product"].values[0]} in {country}? (y/n)')
        if add_quantity.lower() == 'y':
            add_quantity = int(input(f'How many do you want to add?'))
            df.loc[(df['product'] == lowest_obj["product"].values[0]) & (df['country'] == country), 'quantity'] += add_quantity
            print(f'Quantity of {lowest_obj["product"].values[0]} in {country} is now {lowest_obj["quantity"].values[0] + add_quantity}')
        
    df.to_csv('T32/inventory.txt', index=False)

    '''
    This function will find the shoe object with the lowest quantity,
    which is the shoes that need to be re-stocked. Ask the user if they
    want to add this quantity of shoes and then update it.
    This quantity should be updated on the file for this shoe.
    '''

def search_shoe(self):
    shoe_code = int(input('Enter shoe code'))
    # for shoe in shoe_list:
    if shoe_code in shoe_list:
        print (shoe_code)
        

def create_shoe():
    v1 = input("Enter country: ")
    v2 = input("Enter code: ")
    v3 = input("Enter product: ")
    v4 = int(input("Enter cost: "))
    v5 = int(input("Enter qty: "))

    # shoe = {
    #                 'country': v1,
    #                 'code': v2,
    #                 'product': v3,
    #                 'cost': v4,
    #                 'quantity': v5
    #             }
    # shoe_list.append(shoe)
    
    shoe_2 = Shoe(v1, v2, v3, v4, v5)
    shoe_list.append(shoe_2)
'''
     This function will search for a shoe from the list
     using the shoe code and return this object so that it will be printed.
'''

def value_per_item(self):
    for shoe in shoe_list:
        value = shoe['cost'] * shoe['quantity']
        print(f"Product: {shoe['product']}, Value: {value}")
    
    '''
    This function will calculate the total value for each item.
    Please keep the formula for value in mind: value = cost * quantity.
    Print this information on the console for all the shoes.
    '''

def highest_qty(self):

    for shoe in shoe_list:
        max_shoe = max(shoe['quantity'])
    print(f'Shoe with the highest qty is', {max_shoe})



    # pass
    '''
    Write code to determine the product with the highest quantity and
    print this shoe as being for sale.
    '''
# read_shoes_data() # Reads shoe data and create a shoe object





# search_shoe()
#==========Main Menu=============
'''
Create a menu that executes each function above.
This menu should be inside the while loop. Be creative!
'''

user_selection = ""

while user_selection != "quit":
    user_selection = int(input("What would you like to do today?\
        1 - read shoe inventory\
        2 - create new inventory \
        3 - find a shoe\
        4 - restock\
        5 - print shoe value\
        6 - put shoe for sale "))

    if user_selection == 1:
        # read_shoes_data(1)
        # view = Shoe()
        view_all()

    
    elif user_selection == 2:
        create_shoe()
        # NOTE: Ensure to write the shoe back to the file as an appended item

        # __str__ = Shoe()
        # view = Shoe()
        # view.capture_shoes()
