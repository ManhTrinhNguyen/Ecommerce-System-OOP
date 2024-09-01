from shopping_cart import Shopping_Cart 
from order import Order
from product import Product

class Customer: 
  # Instances Attribute 
  def __init__(self, customer_id: int, name: str, email: str) -> None:
    self.customer_id = customer_id
    self.name = name 
    self. email = email
    self.cart = Shopping_Cart() # A `ShoppingCart` object that represents the customer's current shopping cart.

  # Add product to cart 
  def add_to_cart(self, product, quantity): 
    # Check if the amount of stock available to add to cart 
    if product.reduce_stock(quantity): # Use reduce_stock method from Product class . The reason reducing stock is take the stock from Product to the customer cart 
      return self.cart.add_product(product, quantity) # Use add_product method from Shopping_Cart class 
      
  # Remove product from cart 
  def remove_from_cart(self, product):
    quantity = self.cart.items.get(product) # Check the quantity of the Product 
    if quantity > 0: # Check there is product in cart 
      product.increase_stock(quantity) # use increase_stock from Product class to increase stock back to the Product
      return self.cart.remove_product(product) # use the remove_product from Shopping_cart class to remove product
  
  # View the cart 
  def view_cart(self):
    return self.cart.items
  
  # Check out 
  def checkout(self): 
    if self.cart.get_total() > 0:
      order = Order(self, self.cart.items) # Create Order by using Order class 
      order.update_status('Shipped')
      return order




product1 = Product(1, "Laptop", 999.99, 10)
product2 = Product(2, "Smartphone", 499.99, 5)
customer1 = Customer(101, "Alice", "alice@example.com")
customer1.add_to_cart(product1, 1)
customer1.add_to_cart(product2, 1)
print(customer1.checkout())