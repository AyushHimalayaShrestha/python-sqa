# inventory management
class Product:
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity

class Inventory:
    def __init__(self):
        self.items = []

    def add_item(self, product):
        self.items.append(product)

    def show_inventory(self):
        for p in self.items:
            print(f"{p.name} - {p.quantity}")

inv = Inventory()
inv.add_item(Product("Laptop", 10))
inv.add_item(Product("Phone", 25))
inv.show_inventory()
