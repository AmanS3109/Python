class Item:
    def __init__(self, name: str, price: int, quantity: int):
        assert price > 0, f"Price {price} is not greater than 0"
        assert quantity > 0, f"Quantity {quantity} is not greater than 0"
        self.name = name
        self.price = price
        self.quantity = quantity


    def calculate_total_price(self):
        return self.price * self.quantity


item_1 = Item("Phone", 500, -5)

item_2 = Item("Laptop", 1000, -3)

print(item_1.name)
print(item_2.name)
print(item_1.price)
print(item_2.price)
print(item_1.quantity)
print(item_2.quantity)
print(item_1.calculate_total_price())
print(item_2.calculate_total_price())
