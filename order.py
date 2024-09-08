class Order:
    all_orders = []

    def __init__(self, customer, coffee, price):
        if not isinstance(price, float) or not (1.0 <= price <= 10.0):
            raise ValueError("Price must be a number between 1.0 and 10.0")

        self._customer = customer
        self._coffee = coffee
        self._price = price

        customer.orders_list.append(self)
        coffee.order_list.append(self)
        Order.all_orders.append(self)

    @property
    def price(self):
        return self._price

    @property
    def customer(self):
        return self._customer

    @property
    def coffee(self):
        return self._coffee

