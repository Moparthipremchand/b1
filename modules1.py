import requests
apiurl="https://jsonplaceholder.typicode.com/posts"
response=requests.get(apiurl)
# print(response)

if response.status_code==200:
    content=response.json()
    # print(type(content))
# Fetch all posts and print the total number of posts returned. 
    for i in content:
        print(i)
        
# Fetch the post with id = 15 and print its title only.
        if i["id"]==15:
            print(i["title"])
            
# Fetch all posts where userId = 3 and print the count of those posts.
    count = 0
    for i in content:
        if i["userId"]==3:
            count+=1
    print("Number of posts with userId = 3:", count) 
    
# Fetch the post with id = 50 and print both title and body
    for i in content:
        if i["id"]==50:
            print("title :",i["title"])
            print("body :",i["body"])
            
# Fetch all posts for userId = 7 and display only the id values of those posts.
    for i in content:
        if i["userId"]==7:
            print("id :",i["id"])
            












import requests
apiurl="https://jsonplaceholder.typicode.com/users"
response=requests.get(apiurl)
# print(response)

if response.status_code==200:
    content=response.json()
    # print(type(content))   
#  Count all users Task: Fetch all users and print the total number of users returned.
    count=0
    for i in content:
        count+=1
    print("users",count)
    
    
#  Get a user by ID Task: Retrieve the user with id = 5 and print their name and email.
    for i in content:
        if i["id"]==5:
            print("name :",i["name"])
            print("mail :", i["email"])
            
#  Filter users by username Task: Fetch user(s) with username = "Bret" and print the entire JSON object for the match.
    for i in content:
        if i["username"]=="Bret":
            print(i)
            
#Search users by city in address Task: Retrieve all users and print the names of those whose address.city is "South Christy".
    for i in content:
        if i["address"]["city"]=="South Christy":
            print(i)
            
#List user IDs by company name Task: Fetch all users and print the id of each user whose company.name contains the word "Group".
    for i in content:
        if "Group" in i["company"]["name"]:
            print(i)
            
            













import requests
apiurl=" https://jsonplaceholder.typicode.com/todos"
response=requests.get(apiurl)
# print(response)

if response.status_code==200:
    content=response.json()
    # print(type(content))   
    
#Count all todos Task: Send a GET request to /todos and print the total number of todo items returned.
    count=0
    for i in content:
        count+=1
    print("the total number of",count)
    
    
#Get a specific todo by ID Task: Use a GET request to fetch the todo with id = 42 and print its title.
    for i in content:
        if i["id"]==42:
            print(i["title"])
            
#Filter todos by userId Task: Send a GET request with userId=3 (e.g., ?userId=3) and print how many todos belong to that user.
    count=0
    for i in content:
        if i["userId"]==3:
            count+=1
    print(count)
    
    
#List incomplete todos Task: Retrieve all todos and print the ids of todos where completed is false.
    for i in content:
        if i["completed"]==False:   
            print(i)
            
#Count completed todos for a user Task: Fetch todos for userId=5 and count how many of those have completed = true.
    count=0
    for i in content:
        if i["completed"]==True:
            count+=1
            if i["userId"]==5:  
                    print(i)       
    print("completed :",count)
           