# Library
from typing import List

#Describe product class
class Product:
   def __init__(self, name: str, cost: float):
       self.name = name
       self.cost = cost
   def __repr__(self):
      return f"('{self.name}', {self.cost})"

# Functions
def get_product(requestName: str, products: List[Product]) -> bool:
    for product in products:
      if product.name.lower() == requestName.lower():
         return True
    return False

def get_cost(requestName: str, products: List[Product]) -> float:
    for product in products:
      if product.name.lower() == requestName.lower():
         return product.cost
    return 0.0

def get_total(productsCost: List[float]) -> float:
    total = 0
    for cost in productsCost:
       total = cost + total
    return total

#Products in stock.
products = [
   Product("Soda", 3.00),
   Product("Chetos", 2.50),
   Product("Gummys", 2.00)
]
shopList = []
cost = []
# Request product to the client.
while True:
  print("Write the name of the product")
  productName = input().strip()
 # Print the ticket.
 # Is the product in the stock?
  exists = get_product(productName, products)
  if exists:
    productCost = get_cost(productName, products)
    sellProduct = Product(productName, productCost)
    shopList.append(sellProduct)
    cost.append(productCost)
    print ("Your shopping list:", shopList)
    print("Continue? Yes or No")
    responseClient = input().strip()
    if responseClient.lower() == 'yes':
       continue
    else:
       print ("Your shopping list:", shopList)
       print("Total:", get_total(cost))
       break
  else:
    print ("we haven't this product in the stock.")