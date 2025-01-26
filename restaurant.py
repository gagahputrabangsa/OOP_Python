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

    def view_order(self):
        if not self.items:
            print("Your order is empty!")
        else:
            print("\nYour Order:")
            for index, item in enumerate(self.items, start=1):
                print(f"{index}. {item}")
            print(f"Total: ${self.calculate_total():.2f}")

    def calculate_total(self):
        return sum(item.price for item in self.items)

    def clear_order(self):
        self.items = []
        print("Order cleared.")


