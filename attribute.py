class Item:
    pay_rate = 0.8 # 80% pay rate
    all = []

    def __init__(self, name: str, price: int, quantity: int):
        assert price > 0, f"Price {price} is not greater than 0"
        assert quantity > 0, f"Quantity {quantity} is not greater than 0"
        self.name = name
        self.price = price
        self.quantity = quantity

        # Actions to execute
        Item.all.append(self)

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = int(self.price * self.pay_rate)
        
    def __repr__(self):
        return f"Item('{self.name}', {self.price}, {self.quantity})"


item_1 = Item("Phone", 500, 5)
item_2 = Item("Laptop", 1000, 3)
item_3 = Item("Headphones", 200, 3)
item_4 = Item("Keyboard", 150, 3)
item_5 = Item("Monitor", 600, 3)

# for instance in Item.all:
# print(instance.name)
print(Item.all)
# print(Item.__dict__)  # print the namespace of the class
# print(item_1.__dict__)  # print the namespace of the instance
