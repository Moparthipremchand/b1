##Zepto – Grocery Delivery

class order:
    tax=50
    def __init__(self, id, items, amount):
        self.order_id=id
        self.items=items 
        self.amount=amount
    def showorder(self):
        print(f"order id {self.order_id} item is {self.items}" f"and the  total amount is including tax {self.amount + self.tax}")
        pass
        
        
class delivery(order):
    def __init__(self, id, items, amount):
        super().__init__(id, items, amount )
        
    def delstatus(self):
        # print(f"your order id is {self.order_id} item name {self.items} and amount is {self.amount}")
        super().showorder()
        
        
obj=order(3,"pizza",150)  
obj1=delivery(2,"biryani",200)
obj1.delstatus()
obj.showorder()

# print(obj2)
# print(obj3)



##Amazon – E-commerce 



class product:
    platform="amazon"
    def __init__(self,n , p, c):
        self.p_name=n
        self.price=p
        self.category=c
        
    def showproducts(self):
        print(f"produt name {self.p_name} and price {self.price} and category {self.category} from {self.platform}")
        
class discountproduct(product):
    tax=int(input("enter discount"))
    dis=(tax/100)
    def __init__(self,n, p, c):
        super().__init__(n , p, c)
        
    # tax=int(input("enter discount"))
    # dis=(tax/100)
        
    def disper(self):
        tax=int(input("enter discount"))
        dis=(tax/100)
        finalprice=self.price-(self.price*dis)
        
        # self.tax=t
        # self.dis=d
        
        print(f"produt name {self.p_name} and final price {finalprice} and category {self.category} from {self.platform}")
        

obj=product("mobile", 25000, "electronics")  
obj2=discountproduct("mobile", 25000, "electronics")

obj.showproducts()
obj2.disper()
        
        
## Uber – Ride Booking 

class rider:
    def __init__(self, id, p_loc, d_loc):
         self.ride_id=id
         self.pickup=p_loc
         self.drop=d_loc
         
    def showrider(self):
        distanc=12
        print(f"ride id is {self.ride_id} and pickup location from {self.pickup} to drop locatin {self.drop} total distance in km={distanc}")


class driver(rider):
    def __init__(self, id, p_loc, d_loc):
        super().__init__(id, p_loc, d_loc)
        
    def show_driver(showrider):
        print("driver is arriving yor location in 5 minutes")
        
obj=driver(1234, "kukatpally", "hitechcity")
obj.showrider()
obj.show_driver()