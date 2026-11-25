# Scenario: A shopping app stores store-wide, product-specific, and temporary values.
tax_rate = 0.18                 # global/module-level variable

class Product:
    store_name = "Campus Store" # class (static) variable

    def __init__(self, name, price):
        self.name = name        # instance variable
        self.price = price

    def final_price(self):
        discount = 50            # local variable
        return self.price + self.price * tax_rate - discount

item = Product("Backpack", 1200)
print("Store:", Product.store_name)
print("Product:", item.name)
print("Final price:", round(item.final_price(), 2))
