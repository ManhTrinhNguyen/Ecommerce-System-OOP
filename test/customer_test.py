import sys 
sys.path.insert(1, '/Users/trinhnguyen/Documents/Meta-Certificate/Python/object-oriented-programing/Ecommerce-System-OOP/Ecommerce-System-OOP')

from product import Product
from customer import Customer
from order import Order

class Test_Customer: 
  def setup_method(self, method):
    print(f"Setting up method {method}")
    self.customer = Customer(101, "Alice", "alice@example.com")
    self.product = Product(1, "Laptop", 999.99, 10)

  def test_add_to_cart(self):
    assert self.customer.add_to_cart(self.product, 5) == "Laptop added to the cart with 5 quantity"
    assert self.customer.add_to_cart(self.product, 1) == "Laptop already in the cart. Add 1 Laptop to cart now have: 6 in stocks"
    assert self.customer.add_to_cart(self.product, 10) == None # Product only have 4 in stocks left . Cannot add to card more . Return None 
  
  def test_remove_from_cart(self):
    # Add product to cart 
    assert self.customer.add_to_cart(self.product, 5) == "Laptop added to the cart with 5 quantity"
    # Remove product from cart 
    assert self.customer.remove_from_cart(self.product) == "Removed Laptop from cart"

  def test_view_cart(self):
    # Nothing in cart 
    assert self.customer.view_cart() == {}
    # Add product to cart 
    assert self.customer.add_to_cart(self.product, 5) == "Laptop added to the cart with 5 quantity"
    # Laptop in cart 
    assert self.customer.view_cart() == {self.product: 5}
    # Remove product from cart 
    assert self.customer.remove_from_cart(self.product) == "Removed Laptop from cart"
    # Nothing in cart 
    assert self.customer.view_cart() == {}
    
  def test_checkout(self):
    
    # Nothing in cart 
    assert self.customer.checkout() == 'Your cart is empty'
    # Add product to cart 
    assert self.customer.add_to_cart(self.product, 5) == "Laptop added to the cart with 5 quantity"
    # Laptop in cart with 5 quantity
    order = Order(self.customer, self.customer.cart.items.copy())
    assert self.customer.checkout() == order