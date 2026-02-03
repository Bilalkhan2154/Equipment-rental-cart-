class Equipment:
    def __init__(self, name, price_per_day, quantity):
        self.name = name
        self.price_per_day = price_per_day
        self.quantity = quantity

class Inventory:
    def __init__(self):
        self.items = {
            "Camera": Equipment("Camera", 1500, 5),
            "Lens": Equipment("Lens", 800, 10),
            "Tripod": Equipment("Tripod", 300, 7),
            "Light": Equipment("Light", 500, 8),
            "Microphone": Equipment("Microphone", 400, 6)
        }

    def display(self):
        print("\n--- Available Equipment ---")
        for item in self.items.values():
            print(f"{item.name} | Price/day: QR{item.price_per_day} | Available: {item.quantity}")

class Cart:
    def __init__(self):
        self.cart_items = {}

    def add_item(self, equipment, qty):
        if equipment.quantity < qty:
            print("Not enough quantity available.")
            return

        equipment.quantity -= qty

        if equipment.name in self.cart_items:
            self.cart_items[equipment.name]["qty"] += qty
        else:
            self.cart_items[equipment.name] = {
                "price": equipment.price_per_day,
                "qty": qty
            }

        print(f"✔ Added {qty}x {equipment.name} to cart.")

    def remove_item(self, equipment):
        if equipment.name not in self.cart_items:
            print("Item not in cart.")
            return

        qty = self.cart_items[equipment.name]["qty"]
        equipment.quantity += qty
        del self.cart_items[equipment.name]

        print(f"✔ Removed all {equipment.name} from cart.")

    def view_cart(self):
        print("\n--- Your Rental Cart ---")
        if not self.cart_items:
            print("Cart is empty.")
            return

        total = 0
        for name, details in self.cart_items.items():
            amount = details["price"] * details["qty"]
            total += amount
            print(f"{name} | Qty: {details['qty']} | Price/day: ₹{details['price']} | Subtotal: ₹{amount}")

        print(f"\nTOTAL RENT PER DAY: ₹{total}")

    def checkout(self):
        if not self.cart_items:
            print("❌ Cart is empty.")
            return
        
        print("\n🎉 Checkout Successful! Your items are booked.")
        self.view_cart()
        self.cart_items.clear()

inventory = Inventory()
cart = Cart()

def menu():
    while True:
        print("\n========= Camera Equipment Rental =========")
        print("1. View Available Equipment")
        print("2. Add Item to Cart")
        print("3. Remove Item from Cart")
        print("4. View Cart")
        print("5. Checkout")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            inventory.display()

        elif choice == "2":
            item_name = input("Enter item name to add: ").title()
            if item_name not in inventory.items:
                print("❌ Item not found.")
                continue

            qty = int(input("Enter quantity: "))
            cart.add_item(inventory.items[item_name], qty)

        elif choice == "3":
            item_name = input("Enter item name to remove: ").title()
            if item_name not in inventory.items:
                print("❌ Item not found.")
                continue

            cart.remove_item(inventory.items[item_name])

        elif choice == "4":
            cart.view_cart()

        elif choice == "5":
            cart.checkout()

        elif choice == "6":
            print("Thank you for using the rental system!")
            break

        else:
            print("Invalid choice. Try again.")

menu()
