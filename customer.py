class Customer:
    def __init__(self,name):
        self.name = name
        self.orders_list =[]

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value,str) or not (1 <= len(value) <= 15):
            raise ValueError("Names must be between 1 and 15 characters, inclusive")
        self._name = value

    def order(self):
        return self.orders_list

    def coffee(self):
        return list(set([order.coffee for order in self.orders_list]))

    def create_order(self, coffee, price):
        from .order import Order
        order = Order(self, coffee, price)
        self.orders_list.append(order)
        return order
