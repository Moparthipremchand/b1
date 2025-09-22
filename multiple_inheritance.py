# ##Multiple Inheritance in Uber

# class person:
#     def __init__(self):
#         self.name="Rahul"
#         self.contact="9876543210"
        
#     def person_details(self):
#         print(f"person name {self.name} and his contact number is {self.contact}")
        
# class driver:
#     def __init__(self):
#         self. license_no= "DLX12345"
#         self.rating=4.9
        
#     def driver_details(self):
#         print(f"licience number is {self.license_no} and rating from from 1 to 5 is {self.rating}")
        
        
# class UberDriver(person, driver):
#     def __init__(self):
#         self.carname="Hyundai i20"
#         person.__init__(self)
#         self.person_details()
#         driver.__init__(self)
#         self.driver_details()
        
#     def car(self):
#         print(f" care name is {self.carname}")
        
# ud=UberDriver()
# ud.car()




##Multiple Inheritance in Blinkit 

class person1:
    def __init__(self):
        self.name= "Anil"
        self.contact="9876543210"
        
    def person1_details(self):
        print(f"person name is {self.name} and hi contact number is {self.contact} ")
        
        
class Employee:
    def __init__(self):
        self.id="BKP101"
        self.salery=12000 
        
    def employee_details(self):
        print(f"employ id : {self.id}  employ salery : {self.salery}")
        
        
class  DeliveryPartner(person1, Employee):
    def __init__(self):
        self.vehicle= "Scooter"
        person1.__init__(self)
        self.person1_details()
        Employee.__init__(self)
        self.employee_details()
        
    def shodetails(self):
        print(f"delivery vehicel is {self.vehicle}")
        
        
abc=DeliveryPartner()
abc.shodetails()
