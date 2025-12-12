# main.py
from sweet import SweetShop

def display_menu():
    print("\n====== SWEET SHOP MANAGEMENT SYSTEM ======")
    print("1. Add Sweet")
    print("2. Delete Sweet")
    print("3. View All Sweets")
    print("4. Sort Sweets")
    print("5. Purchase Sweet")
    print("6. Restock Sweet")
    print("7. Search Sweets")
    print("8. Exit")

def display_search_menu():
    print("\n--- Search Sweets ---")
    print("1. Search by Name")
    print("2. Search by Category")
    print("3. Search by Price Range")
    print("4. Back to Main Menu")

def main():
    shop = SweetShop()

    while True:
        display_menu()
        choice = input("Enter your choice (1-8): ")

        # add sweet

        if choice == '1':
            print("\n-- Add Sweet --")
            id = input("Enter sweet id: ")
            name = input("Enter sweet name: ")
            category = input("Enter category: ")
            price = input("Enter price: ")
            quantity = input("Enter quantity: ")

            # Validation check
            if not id or not name or not category or not price or not quantity:
                print("❌ Error: All fields are required!")
                continue

            try:
                id=int(id)
                price = float(price)
                quantity = int(quantity)
                shop.add_sweet(id,name,  category, price, quantity)
                print("✅ Sweet added successfully!")
            except ValueError:
                print("❌ Invalid price or quantity format.")

        # delete byname 

        elif choice == '2':
            try:
                print("\n-- Delete Sweet --")
                name= input("Enter sweet name to delete: ")
                shop.delete_sweet(name)
                print("✅ Sweet deleted.")
            except ValueError:
                print("❌ Sweet not found.")

        # view sweets

        elif choice == '3':
            print("\n-- View Sweets --")
            sweets = shop.view_sweets()
            if not sweets:
                print("ℹ️ No sweets available.")
            else:
                for s in sweets:
                    print(s)

        # Short sweet by name,category,prce and quantity

        elif choice == '4':
            print("\n-- Sort Sweets --")
            by = input("Sort by (name/category/price/quantity): ").lower()
            try:
                sorted_sweets = shop.sort_sweets(by)
                for s in sorted_sweets:
                    print(s)
            except KeyError:
                print("❌ Invalid field to sort by.")

        # Purchase sweet

        elif choice == '5':
            try:
                print("\n-- Purchase Sweet --")
                name = input("Enter sweet name to purchase: ")
                quantity = input("Enter quantity to purchase: ")
                if not quantity.isdigit():
                    print("❌ Quantity must be a number.")
                    continue
                quantity = int(quantity)
                shop.purchase_sweet(name, quantity)
                print(f"✅ Purchased {quantity} of {name}")
            except ValueError:
                print("❌ Not enough stock or sweet not found.")

        # Restock sweet

        elif choice == '6':
            try:
                print("\n-- Restock Sweet --")
                name = input("Enter sweet name to restock: ")
                qty = input("Enter quantity to restock: ")
                if not qty.isdigit():
                    print("❌ Quantity must be a number.")
                    continue
                qty = int(qty)
                shop.restock_sweet(name, qty)
                print(f"✅ Restocked {qty} of {name}")
            except ValueError:  
                print("❌ Sweet not found.")

        # Seacrch sweet

        elif choice == '7':
            while True:
                display_search_menu()
                sub_choice = input("Choose search type (1-4): ")

                if sub_choice == '1':
                    name = input("Enter name to search: ")
                    results = shop.search_sweets(name=name)
                elif sub_choice == '2':
                    category = input("Enter category to search: ")
                    results = shop.search_sweets(category=category)
                elif sub_choice == '3':
                    min_price = input("Enter minimum price: ")
                    max_price = input("Enter maximum price: ")
                    try:
                        min_price = float(min_price)
                        max_price = float(max_price)
                        results = shop.search_sweets(min_price=min_price, max_price=max_price)
                    except ValueError:
                        print("❌ Invalid price values.")
                        continue
                elif sub_choice == '4':
                    break
                else:
                    print("❌ Invalid option.")
                    continue

                if results:
                    for s in results:
                        print(s)
                else:
                    print("ℹ️ No sweets found for the given criteria.")

        elif choice == '8':
            print("👋 Exiting Sweet Shop System. Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please enter a number from 1 to 8.")

if __name__ == "__main__":
    main()
