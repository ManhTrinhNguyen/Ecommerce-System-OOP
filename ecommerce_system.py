from order import Order
from product import Product
from customer import Customer

class Ecommerce_System:
  # Instances Attribute 
  def __init__(self) -> None:
    self.products = [] # A list of all Product objects available in the system.
    self.customers = [] # A list of all Customer objects registered in the system.
    self.orders = [] # A list of all Order objects placed in the system.

  # Method 
  def add_product(self, product): # Add new product to the system 
    self.products.append(product)

  def add_customer(self, customer):
    self.customers.append(customer)

  def create_order(self, customer): # Creates an order for the given customer based on their cart.
    order = customer.checkout() # create order from customer checkout function  
    if order: # If true append to orders list
      return self.orders.append(order)
    
  def view_orders_by_customer(self, customer_id): # returns a list of all orders placed by a given customer.
    for order in self.orders:
      if order.customer.customer_id == customer_id:
        return [order]    

# Create products
product1 = Product(1, "Laptop", 999.99, 10)
product2 = Product(2, "Smartphone", 499.99, 5)
product3 = Product(3, "Headphones", 199.99, 20)

# Create customers
customer1 = Customer(101, "Alice", "alice@example.com")
customer2 = Customer(102, "Bob", "bob@example.com")

# Create e-commerce system
ecommerce = Ecommerce_System()

ecommerce.add_product(product1)
ecommerce.add_product(product2)
ecommerce.add_product(product3)

## Add Customer 
ecommerce.add_customer(customer1)
ecommerce.add_customer(customer2)

# Add products to customers' carts
customer1.add_to_cart(product1, 1)
customer1.add_to_cart(product3, 2)
customer2.add_to_cart(product2, 1)
customer2.add_to_cart(product1, 3)

ecommerce.create_order(customer1)

# Check product stock after checkout
print(product1)

# View orders by customer1
print(ecommerce.view_orders_by_customer(101))
# Update the order status
order1 = ecommerce.orders[0]
order1.update_status("Shipped")
print(order1)