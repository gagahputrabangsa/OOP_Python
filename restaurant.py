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

class Restaurant:
    def __init__(self, name):
        self.name = name
        self.menu = []

    def add_menu_item(self, menu_item):
        self.menu.append(menu_item)

    def display_menu(self):
        if not self.menu:
            print("The menu is empty!")
        else:
            print(f"\n{self.name} Menu:")
            for index, item in enumerate(self.menu, start=1):
                print(f"{index}. {item}")

# Example Usage
if __name__ == "__main__":
    # Create a restaurant and add menu items
    restaurant = Restaurant("The Gourmet Spot")
    restaurant.add_menu_item(MenuItem("Burger", 8.99, "A juicy beef burger with lettuce, tomato, and cheese."))
    restaurant.add_menu_item(MenuItem("Pizza", 12.99, "12-inch margherita pizza with fresh mozzarella and basil."))
    restaurant.add_menu_item(MenuItem("Salad", 7.49, "A fresh garden salad with a choice of dressing."))
    
    # Display the menu
    restaurant.display_menu()
    
    # Create an order
    order = Order()



