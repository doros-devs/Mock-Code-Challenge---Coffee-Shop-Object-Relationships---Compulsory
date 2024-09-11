class Customer:
    def __init__(self, name):
        if isinstance(name, str) and 1 <= len(name) <= 15:
            self._name = name
        else:
            raise ValueError("Name must be a string between 1 and 15 characters.")
        self._orders = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_person):
        if isinstance(new_person, str) and 1 <= len(new_person) <= 15:
            self._name = new_person
        else:
            raise ValueError("Names must be between 1 and 15 character")

    def orders(self):
        return self._orders

    def coffees(self):
        return list(set(order.coffee for order in self._orders))

    def create_order(self, coffee, price):
        from order import Order
        order = Order(self, coffee, price)
        self._orders.append(order)
        coffee.add_order(order)
        return order