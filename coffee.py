class Coffee:
    def __init__(self, name):
        if not isinstance(name, str) or len(name) < 3:
            raise ValueError("Names length must be greater or equal to 3 characters")
        self._name = name
        self.order_list = []

    @property
    def name(self):
        return self._name

    def orders(self):
        return self.order_list

    def coffee(self):
        return list(set([order.customer for order in self.order_list]))

    def num_orders(self):
        return len(self.order_list)

    def average_price(self):
        if not self.order_list:
            return 0
        all_prices = sum(order.price for order in self.order_list)
        return all_prices / len(self.order_list)