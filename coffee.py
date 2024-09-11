class Coffee:
    def __init__(self, name):
        if isinstance(name, str) and len(name) >= 3:
            self._name = name
        else:
            raise ValueError("Names length must be greater or equal to 3 characters")
        self._orders = []

    @property
    def name(self):
        return self._name

    def orders(self):
        return self._orders

    def customers(self):
        return list(set(order.customer for order in self._orders))

    def add_order(self, order):
        self._orders.append(order)

    def num_orders(self):
        return len(self._orders)

    def average_price(self):
        if not self._orders:
            return 0
        total_price = sum(order.price for order in self._orders)
        return total_price / len(self._orders)