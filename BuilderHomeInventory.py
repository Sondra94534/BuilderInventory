"""
BuilderHomeInventory.py: Basic implementation for managing a home inventory using Python.
"""
__author__= "Sondra Hoffman"

import csv
import os

emp_dict = {}
prompt = 'Select: 1. add a new home, 2. remove a home, 3. update a home, 4. output inventory to CSV file, 5. exit>>'

class BuilderInventory:
    # Constructor
    def __init__(self, square_ft=None, address=None, city=None, state=None, zip_code=None, model_name=None, sales_status=None):
        self.square_ft = square_ft
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.model_name = model_name
        self.sales_status = sales_status
        
    def build_inventory(self):
        while True:
            print("Menu:")
            print("1. Add a new home")
            print("2. Remove a home")
            print("3. Update a home")
            print("4. Output inventory to CSV file")
            print("5. Exit")

            choice = input("Select an option: ")
        
            if choice == "1":
                self.add_house()
            elif choice == "2":
                self.remove_home()
            elif choice == "3":
                self.update_home()
            elif choice == "4":
                self.output_to_csv()
            elif choice == "5":
                break
            else:
                print("Invalid choice. Please select a valid option.")

    print("Inventory building process completed.")

            
    def add_house(self):
        """
        Method to add a new home to the inventory.
        Prompts the user for details and stores the information in the inventory dictionary.
        """
        while True:
            key_str = input('Input name (ENTER to exit): ')
            key_str = key_str.strip()
            if not key_str:
                return
            square_ft = int(input('Enter the square feet: '))
            address = input('Enter the address: ')
            city = input('Enter the city: ')
            state = input('Enter the state: ')
            zip_code = int(input('Enter the zipcode: '))
            model_name = input('Enter the model name: ')
            sales_status = input('What is the sales status: ')
            emp_dict[key_str] = BuilderInventory(square_ft, address, city, state, zip_code, model_name, sales_status)
            
    def remove_home(self):
        """
        Method to remove a home from the inventory.
        Prompts the user for the name of the home to remove and deletes it from the inventory dictionary.
        """
        while True:
            key_str = input('Input name (ENTER to exit): ')
            key_str = key_str.strip()
            if not key_str:
                return
            if key_str in emp_dict:
                del emp_dict[key_str]
                print('Home removed.')
            else:
                print('Home not found.')
                
    def update_home(self):
        """
        Method to update the details of a home in the inventory.
        Prompts the user for the name of the home to update and allows them to modify its details.
        """
        while True:
            key_str = input('Input name (ENTER to exit): ')
            key_str = key_str.strip()
            if not key_str:
                return
            if key_str in emp_dict:
                square_ft = int(input('Enter the square feet: '))
                address = input('Enter the address: ')
                city = input('Enter the city: ')
                state = input('Enter the state: ')
                zip_code = int(input('Enter the zipcode: '))
                model_name = input('Enter the model name: ')
                sales_status = input('What is the sales status: ')
                emp_dict[key_str] = BuilderInventory(square_ft,

 address, city, state, zip_code, model_name, sales_status)
                print('Home updated.')
            else:
                print('Home not found.')
    
    def output_to_csv(self):
        """
        Method to output the home inventory to a CSV file.
        Prompts the user for the filename and writes the inventory data to a CSV file with appropriate headers.
        """
        filename = input('Enter the filename for the CSV output: ')
        filename = os.path.join(os.path.expanduser("~"),"path and file name is input here", filename)

        fieldnames = ['Name', 'Square Feet', 'Address', 'City', 'State', 'Zip Code', 'Model Name', 'Sales Status']
        with open(filename, 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for name, home in emp_dict.items():
                writer.writerow({
                    'Name': name,
                    'Square Feet': home.square_ft,
                    'Address': home.address,
                    'City': home.city,
                    'State': home.state,
                    'Zip Code': home.zip_code,
                    'Model Name': home.model_name,
                    'Sales Status': home.sales_status
                })
        print('Inventory exported to CSV file.')

def main():
    """
    Main function to create a BuilderInventory object and build the inventory.
    """
    inventory = BuilderInventory()
    inventory.build_inventory()

if __name__ == '__main__':
    main()