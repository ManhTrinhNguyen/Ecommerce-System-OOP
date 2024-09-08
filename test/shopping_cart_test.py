import sys 
sys.path.insert(1, '/Users/trinhnguyen/Documents/Meta-Certificate/Python/object-oriented-programing/Ecommerce-System-OOP/Ecommerce-System-OOP')

from shopping_cart import Shopping_Cart 
from product import Product

class Test_Shopping_Cart:
  def setup_method(self, method):
    print(f'Setting up {method}')
    self.shopping_cart = Shopping_Cart()
    self.product = Product(1, "Laptop", 999.99, 10)
    self.product2 = Product(2, "Smartphone", 499.99, 5)

  def test_add_product(self):
    # Nothing in the cart . Added Laptop to cart
    assert self.shopping_cart.add_product(self.product, self.product.quantity) == "Laptop added to the cart with 10 quantity"
    # Laptop already in the cart and add 5 more 
    assert self.shopping_cart.add_product(self.product, 5) == "Laptop already in the cart. Add 5 Laptop to cart now have: 15 in stocks"

  def test_remove_product(self):
    # Nothing in the cart 
    assert self.shopping_cart.items == {}
    # Added Laptop to cart
    assert self.shopping_cart.add_product(self.product, self.product.quantity) == "Laptop added to the cart with 10 quantity"
    # Remove Laptop from cart
    assert self.shopping_cart.remove_product(self.product) == "Removed Laptop from cart"
    # Now nothing in the cart
    assert self.shopping_cart.items == {}
    # Remove Smartphone but it not in the cart 
    assert self.shopping_cart.remove_product(self.product2) == "Smartphone is not in the cart"

  def test_get_total(self):
    # Nothing in the cart 
    assert self.shopping_cart.get_total() == "Your cart is empty"
    # Added 1 Laptop to cart
    assert self.shopping_cart.add_product(self.product, 1) == "Laptop added to the cart with 1 quantity"
    # Return 999.99 total 
    assert self.shopping_cart.get_total() == 999.99
    # Add Smartphone to cart 
    assert self.shopping_cart.add_product(self.product2, 1) == "Smartphone added to the cart with 1 quantity"
    # Total of smartphone and laptop 
    assert self.shopping_cart.get_total() == 1499.98

  def test_clear_cart(self):
    # Added 1 Laptop to cart
    assert self.shopping_cart.add_product(self.product, 1) == "Laptop added to the cart with 1 quantity"
    # Add Smartphone to cart 
    assert self.shopping_cart.add_product(self.product2, 1) == "Smartphone added to the cart with 1 quantity"
    # Total is 1499.98 
    assert self.shopping_cart.get_total() == 1499.98
    # Clear cart 
    assert self.shopping_cart.clear_cart() == "Cart cleared"
    # Total is 0 aflter clear
    assert self.shopping_cart.get_total() == "Your cart is empty"

