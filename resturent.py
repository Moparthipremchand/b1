resturents=[
    {
        "r_name":"house_of_mandi",
        "location":"kukatpally",
        "chicken_items":["dum biryani","fry peace biryani","mogali biryeani","roast biryeani"],
        "soups":["Chicken Noodle Soup","French Onion Soup","Chicken & Rice Soup","Chicken & Sweet Corn Soup","Mulligatawny Soup"],
        "rating":4.3
    },
    {
        "r_name":"aaroma",
        "location":"KPHB",
        "chicken_items":["mutton dum biryani","leg peace biryani","rambo biryeani","skull roast biryeani"],
        "soups":["Mulligatawny Soup","Vegetable Beef Barley Soup","Pho (Vietnamese Noodle Soup)","Chicken Tortilla Soup"],
        "rating":2.9
    },
    {
        "r_name":"eat sure",
        "location":"JNTU",
        "chicken_items":["chicken kaju biryeani","lever biryani","mixed biryeani","guntur hot biryeani"],
        "soups":["Tomato Soup","Butternut Squash Soup","Minestrone","Cream of Mushroom Soup","Mulligatawny Soup"],
        "rating":4.4
    },
    {
        "r_name":"karna",
        "location":"BALA NAGAR",
        "chicken_items":["curry biryani","bone less biryani","mango chicken biryeani","chicken egg biryeani"],
        "soups":["soya soop","ginger garlic soop","fried egg soup","Chicken & Sweet Corn Soup","pannier soup"],
        "rating":3.9
    },
    {
        "r_name":"andhra biryeani house",
        "location":"hitech city",
        "chicken_items":["dum biryani"," special biryani","hot chips biryeani","bambo biryeani"],
        "soups":["chicken bone soup","potat0 Soup","mushroom & Rice Soup","Sweet Corn Soup","Mulligatawny Soup"],
        "rating":4.9
    }
        ]

for i in resturents:
    print("biryeanies :--",i["chicken_items"])
    print("soup :--",i["soups"][3])