from customer import Customer
from coffee import Coffee
from order import Order

def main():
    customers = {}
    coffees = {}

    while True:
        print("\nCoffee Shop Management")
        print("1. Add a customer")
        print("2. Add a coffee")
        print("3. Create an order")
        print("4. View customer orders")
        print("5. View coffee statistics")
        print("6. Exit\n")

        choice = input("Enter your choice: ")

        if choice == "1":
            # Add a customer
            customer_name = input("Enter customer name (1 to 15 characters): ")
            try:
                customer = Customer(customer_name)
                customers[customer_name] = customer
                print(f"Customer '{customer_name}' added successfully!")
            except ValueError as e:
                print(e)

        elif choice == "2":
            # Add a coffee
            coffee_name = input("Enter coffee name (at least 3 characters): ")
            try:
                coffee = Coffee(coffee_name)
                coffees[coffee_name] = coffee
                print(f"Coffee '{coffee_name}' added successfully!")
            except ValueError as e:
                print(e)

        elif choice == "3":
            # Create an order
            customer_name = input("Enter customer name: ")
            coffee_name = input("Enter coffee name: ")
            price = float(input("Enter the price of the coffee (1.0 to 10.0): "))

            if customer_name in customers and coffee_name in coffees:
                customer = customers[customer_name]
                coffee = coffees[coffee_name]
                try:
                    customer.create_order(coffee, price)
                    print(f"Order created for {customer_name} - {coffee_name} (${price})")
                except ValueError as e:
                    print(e)
            else:
                print("Customer or coffee not found. Please add them first.")

        elif choice == "4":
            # View customer orders
            customer_name = input("Enter customer name: ")
            if customer_name in customers:
                customer = customers[customer_name]
                print(f"{customer_name} has ordered:")
                for coffee in customer.coffees():
                    print(f" {coffee.name}")
            else:
                print(f"No customer found with the name '{customer_name}'")

        elif choice == "5":
            # View coffee statistics
            coffee_name = input("Enter coffee name: ")
            if coffee_name in coffees:
                coffee = coffees[coffee_name]
                print(f"{coffee_name} has been ordered {coffee.num_orders()} times.")
                print(f"Average price for {coffee_name}: ${coffee.average_price():.2f}")
                print(f"Customers who ordered {coffee_name}:")
                for customer in coffee.customers():
                    print(f"{customer.name}")
            else:
                print(f"No coffee found with the name '{coffee_name}'")

        elif choice == "6":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()