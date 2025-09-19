##Question 1 – Zomato Food Ordering
## Create a class Restaurant to simulate Zomato’s restaurant system. 
## Requirements: 
## 1. The constructor should accept restaurant_name and menu (dictionary of items → price). 
## 2. Define a method showMenu() that displays all items with prices. 
##        Example: Pizza - ₹200, Burger - ₹120 
## 3. Define a method orderFood(item, qty) that: 
##  Checks if the item is available in the menu. 
##        If available → prints the bill (price * qty). 
##        If not available → prints "Item not available". 
## 4. Create two restaurant objects (Dominos, KFC) with different menus. 
## 5. Place orders from both restaurants.


Dominious={
    "classic pizzas": 149,
    "Golden Corn pizza": 199,
    "Cheese & Tomato pizza":49,
    "Capsicum pizza": 99,
    "Mexican Green Wave": 249,
    " Paneer Makhani.":229,
    "Stuffed Garlic Bread": 150,
    "Chicken Wings": 220,
    "Loaded Tots": 120
    
    }
KFC={
    "Fried Chicken Pieces": 399,
    "chicken hot wings": 279,
    "chicken strips": 129,
    "zinger burger": 99,
    "frinch fries":49,
    "Chicken Roll": 180,
    "Mutton Roll": 220,
    "Paneer Roll": 160
}

class resturent:
    def __init__(self, name, items):
        self.restaurant_name=name 
        self.menu=items
        
    def showMenu(self):
        print(f"\n--- Menu of {self.restaurant_name} ---")
        for item, price in self.menu.items():
            print(f"{item} - ₹{price}")
    
    def orderFood(self, item, qty):
        if item in self.menu:
            total = self.menu[item] * qty
            print(f" You ordered {qty} {item}(s). Bill = ₹{total}")
               
        else:
            print(" Item not available")

                
dominos = resturent("Dominos", Dominious)
kfc = resturent("KFC", KFC)

dominos.showMenu()
kfc.showMenu()

dominos.orderFood("Capsicum pizza", 2)
kfc.orderFood("zinger burger", 3)
kfc.orderFood("Biryani", 1) 


## Question 2 – Uber Ride Booking 
## Create a class Driver to simulate Uber driver details. 
## Requirements: 
## 1. The constructor should accept driver_name, car_model, and per_km_rate. 
## 2. Define a method showDriver() that prints driver details. 
##              o Example: Driver: Raj, Car: Swift, Rate: ₹20/km 
## 3. Define a method calculateFare(distance) that calculates and prints the fare. 
##               o Example: Distance: 10 km, Fare: ₹200 
## 4. Create 3 driver objects with different details. 
## 5. For each driver, calculate fare for a trip (e.g., 8 km, 12 km, 15 km).


class driver:
    def __init__(self,name, car, price):
        self.driver_name=name
        self.carmodel=car 
        self.ride_price=price
        
    def showDriver(self):
        print(f"driver name{self.driver_name} and car model {self.carmodel} car model is {self.ride_price}")
        
    def calculateFare(self, distance, price):
        self.distance=distance
        self.fare_price=price
        
        print(f"distance :--{self.distance}/KM and price for distance is {self.distance * 20}")
        
        
obj1=driver("raju","b3h789", "900000")
obj1.showDriver()
obj1.calculateFare(8,20)

obj2=driver("vikram","volo_g10", "3500000")
obj2.showDriver()
obj2.calculateFare(12,20)

obj3=driver("amar","tata-cv", "1500000")
obj3.showDriver()
obj3.calculateFare(15,20)


## Question 3 – Flipkart Shopping Cart 
## Create a class Product to simulate shopping on Flipkart. 
## Requirements: 
## 1. The constructor should accept product_name, price, and stock. 
## 2. Define a method showDetails() that displays product details. 
## o Example: Laptop - ₹50000, Stock: 10 
## 3. Define a method buyProduct(qty) that: 
## o If enough stock → reduces stock and prints total cost. 
## o If not enough stock → print "Out of Stock". 
## 4. Create 3 product objects (Laptop, Phone, Shoes) with different stock and price. 
## 5. Simulate a shopping cart by: 
## o Buying 2 items from Laptop. 
## o Buying 1 item from Phone. 
## o Trying to buy more Shoes than available stock.

class product:
    def __init__(self, name, price, qnty):
        self.product_name=name 
        self.price=price
        self.stock=qnty
        
    def showDetails(self):
        print(f"product {self.product_name} - {self.price} :  {self.stock}")
        
    def byproduct(self):
        if self.stock > user:
            print(f"{self.product_name} quntaty of items {user} and total price{self.price * user}")
        else:
            print("stock is not available")

user=int(input("enter quantity:--"))      
object1=product("laptops", 50000, 20)
object1.showDetails()
object1.byproduct()

object2=product("mobles", 25000, 10)
object2.showDetails()
object2.byproduct()

object3=product("showes", 700, 2)
object3.showDetails()
object3.byproduct()
