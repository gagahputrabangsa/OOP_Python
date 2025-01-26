class MenuItem:
    def __init__(self, name, price, description):
        self.name = name
        self.price = price
        self.description = description

    def __str__(self):
        return f"{self.name} - ${self.price:.2f} ({self.description})"


class Order:
    def __init__(self):
        self.items = []

    def add_item(self, menu_item):
        self.items.append(menu_item)
        print(f"Added {menu_item.name} to the order.")

