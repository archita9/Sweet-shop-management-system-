class SweetShop:
    def __init__(self):
        # Initialize an empty list to store sweet data
        self.sweets = []


    def add_sweet(self, id, name, category, price, quantity):
        
        #Add a new sweet to the shop. All fields are required.

        if not id or not name or not category or price is None or quantity is None:
            raise ValueError("Missing required sweet fields.")

        self.sweets.append({
            "id": id,
            "name": name,
            "category": category,
            "price": price,
            "quantity": quantity
        })


    def view_sweets(self):

        # Return a list of all available sweets.
        return self.sweets
    

    def delete_sweet(self, name):
        
        #Delete a sweet by its unique ID.
    
        for sweet in self.sweets:
            if sweet["name"] == name:
                self.sweets.remove(sweet)
                return
        raise ValueError("Sweet not found.")
    

    def search_sweets(self, name=None, category=None, min_price=None, max_price=None):
        
        #Search for sweets using optional filters:
        #name, category, min_price, max_price.
        
        results = self.sweets
        if name:
            results = [s for s in results if s["name"].lower() == name.lower()]
        if category:
            results = [s for s in results if s["category"].lower() == category.lower()]
        if min_price is not None:
            results = [s for s in results if s["price"] >= min_price]
        if max_price is not None:
            results = [s for s in results if s["price"] <= max_price]
        return results
    

    def sort_sweets(self, by="price"):
        
        #Sort sweets by price, name, or quantity.
        #Default is by price.
        
        if by not in ["price", "name", "quantity","id","category"]:
            raise ValueError("Invalid sort field. Choose price, name, or quantity.")
        return sorted(self.sweets, key=lambda x: x[by])
    

    def purchase_sweet(self, name, quantity):
        
        #Purchase a sweet by reducing its quantity.
        #Raises error if sweet not found or not enough stock.
        
        for sweet in self.sweets:
            if sweet["name"] == name:
                if sweet["quantity"] < quantity:
                    raise ValueError("Not enough stock available.")
                sweet["quantity"] -= quantity
                return
        raise ValueError("Sweet not found.")
    
    def restock_sweet(self, name, quantity):
        
        #Restock a sweet by increasing its quantity.
        
        for sweet in self.sweets:
            if sweet["name"] == name:
                sweet["quantity"] += quantity
                return
        raise ValueError("Sweet not found.")