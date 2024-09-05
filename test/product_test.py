import sys 
sys.path.insert(1, '/Users/trinhnguyen/Documents/Meta-Certificate/Python/object-oriented-programing/Ecommerce-System-OOP/Ecommerce-System-OOP')

from product import Product
# Create products
# product1 = Product(1, "Laptop", 999.99, 10)
# product2 = Product(2, "Smartphone", 499.99, 5)
# product3 = Product(3, "Headphones", 199.99, 20)

class Test_Product: 
  def setup_method(self, method): # Setup Method at the beginning of each Test 
    print(f"Setting up metohd {method}")
    self.product = Product(1, "Laptop", 999.99, 10)

  def test_reduce_stock(self):
    assert self.product.reduce_stock(5) == True # Reduce 5 stocks . Then 5 stock left
    assert self.product.reduce_stock(6) == False # Only 5 stocks left . Not enough return false 

  def test_increase_stock(self):
    assert self.product.increase_stock(5) == "Added 5 amount of stock" # Add 5 Stocks
    