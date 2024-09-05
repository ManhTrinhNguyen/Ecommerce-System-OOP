class Product:
   # Instances attribute 
  def __init__(self, product_id: int, name: str, price: int, quantity: int) -> None:
    self.product_id = product_id
    self.name = name 
    self.price = price 
    self.quantity = quantity

  # Medthod 
  def __str__(self) -> str:
    return f"Product name: {self.name}, Product_Id: {self.product_id}, Price: {self.price}, Quantity: {self.quantity}"
  
  # Reduce Stock funtion 
  def reduce_stock(self, quantity):
    if self.quantity >= quantity: # Check if Quantity of available stock is greater the given quantity want to reduce 
      self.quantity = self.quantity - quantity # If True => Reduce given quantity want to reduce 
      print(f"Reduced {quantity} amount of stocks")
      return True
    else:
      print(f"Not enough stock to reduce available stock is {self.quantity}") # If false return Not Enough stock 
      return False
    
  # Increase Stock funtion 
  def increase_stock(self, quantity):
    self.quantity = self.quantity + quantity # Add stock by given quantity to original quantity of the product 
    return f"Added {quantity} amount of stock"
