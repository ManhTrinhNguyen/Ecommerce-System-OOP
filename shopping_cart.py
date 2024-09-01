
class Shopping_Cart:
  # Instances Attribute 
  def __init__(self) -> None:
    self.items = {} # A dict where keys are `Product` and value are quantity of those Product 

  # Method 
  # Add Product
  def add_product(self, product, quantity):
    for existing_product in self.items.keys(): # Iterate through dict to get key of dict 
      if existing_product.name == product.name: # Check if product is in the cart by name 
        self.items[existing_product] += quantity # If true => Update the quantity
        return f"{existing_product.name} already in the cart. Add {quantity} {existing_product.name} to cart now have: {self.items[existing_product]} in stocks"
    self.items[product] = quantity # If false => Add product to items dict 
    return f"{product.name} added to the cart with {quantity} quantity"
  
  # Remove Product 
  def remove_product(self, product):
    if product in self.items: # Check if product in the cart
      del self.items[product] # If True remove it
      return f"Removed {product.name} from cart"
    else:
      return f"{product.name} is not in the cart" # If false return "product not in the cart"
    
  # Get total
  def get_total(self):
    total = 0
    if len(self.items) > 0: # Check if the cart is not empty  
      for item in self.items: # Iterate throught the cart 
        total += item.price * self.items[item] # Mutiple price and quantity to take total 
    else: # If the cart is empty return "Your cart is empty"
      return "Your cart is empty"
    
    return total # return total 
  
  # Clear cart 
  def clear_cart(self):
    if len(self.items) > 0: # Check if the cart is not empty 
      self.items.clear() # use clear() to clear all in cart 
      return "Cart cleared"
    else: # If nothing in cart return "Your cart is empty"
      return "Your cart is empty"
    



    

