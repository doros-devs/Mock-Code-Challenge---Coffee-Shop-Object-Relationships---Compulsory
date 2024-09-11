# Mock-Code-Challenge---Coffee-Shop-Object-Relationships---Compulsory

# Coffee Shop Management System

This is a simple coffee shop management system built using Python and Object-Oriented Programming (OOP) principles. The system allows users to manage customers, coffees, and orders, and retrieve useful statistics such as average coffee prices and customer order history.

## Features

- **Add Customers**: Create and manage customers.
- **Add Coffee Options**: Add various types of coffees.
- **Create Orders**: Customers can place orders for coffees with associated prices.
- **View Customer Orders**: Check what coffees a customer has ordered.
- **View Coffee Statistics**: Check how many times a coffee has been ordered and its average price.

## Prerequisites

- Python 3.x
- `virtualenv` or `venv` (to create a virtual environment)

## Installation and Setup

Follow these instructions to set up and run the project on your local machine.

### 1. Clone the repository

First, clone this repository to your local machine:

```bash
git clone <your-private-repo-url>
```

### 2. Navigate into the project directory

```bash
cd <your-project-folder>
```
### 3. Create a virtual environment

```bash
python3 -m venv venv
```
### 4. Activate the virtual environment

On Mac or Linux
```bash
source venv/bin/activate
```

On Windows
```bash
venv\Scripts\activate
```

### 5. Run the Application

To start the application, run the following command:

```bash
python main.py
```

# Usage   

Once the application starts, you’ll be prompted with several options to manage customers, coffees, and orders:

```bash
Coffee Shop Management
1. Add a customer
2. Add a coffee
3. Create an order
4. View customer orders
5. View coffee statistics
6. Exit
```

Sample Interaction

	1.	Add a Customer: Add a customer by providing a name between 1 and 15 characters.
	2.	Add a Coffee: Add a coffee by providing a name with at least 3 characters.
	3.	Create an Order: Associate a customer and a coffee with a price between 1.0 and 10.0.
	4.	View Customer Orders: View all coffees ordered by a specific customer.
	5.	View Coffee Statistics: Get the number of times a coffee has been ordered and its average price.

Here is an example of a session:

```bash
Coffee Shop Management
1. Add a customer
2. Add a coffee
3. Create an order
4. View customer orders
5. View coffee statistics
6. Exit
Enter your choice: 1
Enter customer name (1 to 15 characters): Alice
Customer 'Alice' added successfully!

Enter your choice: 2
Enter coffee name (at least 3 characters): Latte
Coffee 'Latte' added successfully!

Enter your choice: 3
Enter customer name: Alice
Enter coffee name: Latte
Enter the price of the coffee (1.0 to 10.0): 5.0
Order created for Alice - Latte ($5.0)

Enter your choice: 4
Enter customer name: Alice
Alice has ordered:
- Latte

Enter your choice: 5
Enter coffee name: Latte
Latte has been ordered 1 times.
Average price for Latte: $5.00
Customers who ordered Latte:
- Alice

Enter your choice: 6
Goodbye!
```

