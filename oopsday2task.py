## Question 1 – JSONPlaceholder Users → Class Objects 
## Create a class User that stores data fetched from https://jsonplaceholder.typicode.com/users. 
## Requirements: 
## 1. The constructor (__init__) should accept id, name, and email. 
## 2. Define a method showUser() to print the user details in a readable format. 
## o Example: User #1 → Leanne Graham (Sincere@april.biz) 
## 3. Define another method getEmailDomain() to return only the domain part of the email. 
## o Example: april.biz 
## 4. Fetch users from the API and create multiple User objects. 
## 5. Print details of at least 5 users using showUser() and getEmailDomain().




import requests

apiurl="https://jsonplaceholder.typicode.com/users"

response=requests.get(apiurl)
# print(response)

class user:
    def __init__(self, usid, n, e, a, u, w):
        self.id=usid
        self.name=n
        self.email=e
        self.address=a
        self.user_name=u 
        self.web_site=w
        
    def showUser(self):
        print(f"user #{self.id} --> {self.name}  ({self.email})")
        
        
    def getEmailDomain(self):
        email=self.email
        splitmail=email.split("@")
        print(splitmail[1])
    
    def addre(self):
        print(f"user addres {self.address}")
        
    def uname(self):
        print(f"user name is {self.user_name} and his website is {self.web_site}")
        
        
        
        
if response.status_code==200:
    data=response.json()
    for i in data:
        userid=i["id"]
        name=i["name"]
        mail=i["email"]
        address=i["address"]["zipcode"]
        username=i["username"]
        website=i["website"]
        
        obj=user(userid, name, mail, address, username, website)
        
        obj.showUser()
        obj.getEmailDomain()
        obj.addre()
        obj.uname()
    
    
    
    
    
## Question 2 – JSONPlaceholder Posts → Blog System 
## Create a class Post to manage blog posts fetched from https://jsonplaceholder.typicode.com/posts. 
## Requirements: 
## 1. The constructor should accept userId, id, title, and body. 
## 2. Define a method showSummary() that prints the post ID and first 20 characters of the title. 
## o Example: Post #1 → sunt aut facere repellat... 
## 3. Define another method getWordCount() that counts how many words are in the body. 
## 4. Fetch posts from the API and create multiple Post objects. 
## 5. For the first 3 posts, show summary and word count. 




import requests

apiUrl="https://jsonplaceholder.typicode.com/posts"

respons=requests.get(apiUrl)

class  blog_System:
    def __init__(self, userid, idnumber, title, body):
        self.userid=userid
        self.id=idnumber
        self.title=title 
        self.body=body
        
    def showSummary(self):
        print(f"post id--:{self.id}")
        print(f" body {self.body[:20]}")
        
    def getWordCount(self):
        print(f"total charectors in body{len(self.body)}")
        

if respons.status_code==200:
    data=respons.json()
    for i in data:
        userid=i["userId"]
        id=i["id"]
        title=i["title"]
        body=i["body"]
        
        obj1=blog_System( userid, id, title, body)
        obj1.showSummary()
        obj1.getWordCount()






## Question 3 – DummyJSON Products → Flipkart Style 
## Use API: https://dummyjson.com/products 
## Create a class Product to store details of each product. 
## Requirements: 
## 1. The constructor should accept id, title, price, and stock. 
## 2. Define a method showDetails() to display product info. 
## o Example: Laptop (₹50000) – Stock: 12 
## 3. Define another method buyProduct(qty) that reduces stock if enough stock is available, 
## otherwise print "Out of stock". 
## 4. Fetch product data from API and create multiple Product objects. 
## 5. Simulate a shopping cart by buying: 
## o 2 units of the first product. 
## o 1 unit of the second product. 
## o Try buying more than stock for the third product.



import requests

apiurls="https://dummyjson.com/products"

response=requests.get(apiurls)

# print(response)

class products:
    def __init__(self, p_id, p_title, p_price, p_stock):
        self.id=p_id
        self.title=p_title
        self.price=p_price
        self.stock=p_stock
        
    def showdetails(self):
        print(f"{self.title}  ({self.price}) - stock: {self.stock}")
        # Laptop (₹50000) – Stock: 12
        
    def byproducts(self,user_want ,qty):
        self.items=user_want
        self.quantaty=qty
        # print(self.quantaty)
        if self.items == self.title:
            if self.quantaty < self.stock:
                print("your order is processing we will reach you soon")
            else:
                print(f"{self.quantaty} items not in stock we have only {self.stock} items ")
        else:
            print(f"{self.items} is not available ")
    def userbyproduct(self,user_want, qty, itemid):
        self.items=user_want
        self.quantaty=qty
        self.itemid=itemid
        if self.id == itemid:
            if self.stock ==1:
                if self.quantaty < self.stock:
                    print(f"im buying {self.quantaty} items in {self.title} ")
            elif self.stock ==2:
                if self.quantaty < self.stock:
                    print(f"im buying {self.quantaty} items in ")
            else:
                if self.quantaty < self.stock:
                    print(f"im buying {self.quantaty} items in ")
                    
        else:
            ("plese enter below the list oide ")
itemsid_in_list=int(input("enter item id--:"))  
useritem=input("enter ite you want---:")  
stockcheck=int(input("enter how many items you want--:"))      

if response.status_code==200:
    data=response.json()
    maindata=data["products"]
    for i in maindata:
        id_i=i["id"]
        title_t=i["title"]
        price_p=i["price"]
        stock_s=i["stock"]
        
        object3=products(id_i, title_t, price_p, stock_s)
        object3.showdetails()
        object3.byproducts(useritem, stockcheck)
        object3.userbyproduct(useritem, stockcheck, itemsid_in_list)
        
    



