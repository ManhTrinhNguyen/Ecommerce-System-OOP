class Order:
  # Class Attribute
  order_count = 0

  # Instances Attribute 
  def __init__(self, customer, items) -> None:
    Order.order_count += 1
    self.order_id = Order.order_count
    self.customer = customer
    self.items = items
    self.total = sum(product.price * quantity for product, quantity in self.items.items()) # Iterate through items Dict to take key(product) and value(quantity) then mutiply product.price and quantity
    self.status = 'Pending'

  # Method 
  def __str__(self):
    return f"Order({self.order_id}, {self.customer.name}, Total: ${self.total}, Status: {self.status})"

  def update_status(self, new_status): # Update Status 
    self.status = new_status