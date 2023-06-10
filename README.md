# BuilderHomeInventory.py

This program is a basic implementation for managing a home inventory using Python. It allows users to add new homes, remove homes, update home details, and export the inventory to a CSV file.

## Usage

To run the program, execute the following command:

```
python BuilderHomeInventory.py
```

## Features

The program provides the following features:

1. **Add a new home:** Allows users to add a new home to the inventory by providing details such as square footage, address, city, state, zip code, model name, and sales status.

2. **Remove a home:** Enables users to remove a home from the inventory by specifying the name of the home they want to remove.

3. **Update a home:** Allows users to update the details of a home in the inventory. Users can modify information such as square footage, address, city, state, zip code, model name, and sales status.

4. **Output inventory to CSV file:** Allows users to export the home inventory to a CSV file. Users are prompted to enter the filename for the CSV output, and the program writes the inventory data to the file with appropriate headers.

5. **Exit:** Terminates the program.

## Author

This program was developed by Sondra Hoffman.

## Instructions

1. When the program starts, a menu will be displayed with the available options.

2. Select an option by entering the corresponding number and pressing Enter.

3. If you choose to add a new home, you will be prompted to enter the details of the home. Press Enter without typing anything to exit the add home process.

4. If you choose to remove a home, you will be prompted to enter the name of the home you want to remove. Press Enter without typing anything to exit the remove home process.

5. If you choose to update a home, you will be prompted to enter the name of the home you want to update. If the home exists, you will be asked to enter the updated details. Press Enter without typing anything to exit the update home process.

6. If you choose to output the inventory to a CSV file, you will be prompted to enter the filename for the output. The file will be saved in the current directory. Make sure to provide a valid filename.

7. To exit the program, select the "Exit" option from the menu.

## Example

Here's an example scenario to illustrate the program's functionality:

```
Menu:
1. Add a new home
2. Remove a home
3. Update a home
4. Output inventory to CSV file
5. Exit
Select an option: 1

Input name (ENTER to exit): Home1
Enter the square feet: 2000
Enter the address: 123 Main St
Enter the city: Cityville
Enter the state: Stateville
Enter the zipcode: 12345
Enter the model name: Model1
What is the sales status: Sold

Menu:
1. Add a new home
2. Remove a home
3. Update a home
4. Output inventory to CSV file
5. Exit
Select an option: 4

Enter the filename for the CSV output: inventory.csv
Inventory exported to CSV file.

Menu:
1. Add a new home
2. Remove a home
3. Update a home
4. Output inventory to CSV file
5. Exit
Select an option: 5

Inventory building process completed.
```

In this example, a new home named "Home1" is added to the inventory with the provided details. Then, the inventory is exported to a CSV file named "inventory.csv". Finally, the program is exited.

##LICENSE

This project is licensed under the MIT License.
