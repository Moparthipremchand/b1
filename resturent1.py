resturents = {
        "navabs":{
            "veg_items":{
                "biryani": ["mushroom", "kaju", "paneer"],
                "starters": ["veg manchurian", "paneer tikka", "gobi 65"],
                "soups": ["veg soup1", "veg soup2", "veg soup3"]
            },
            "non_veg":{
                "biryani": ["dum", "fry", "moghali", "boneless"],
                "starters": ["chicken tikka", "tandoori", "chilli chicken"],
                "soups": ["nonveg soup1", "nonveg soup2", "nonveg soup3"]
            }
        },
        "vikras":{
            "veg_items":{
                "biryani": ["drumstick biryeani", "egg_biryeani", "gobi"],
                "starters": ["paneer roat", "paneer tikka", "paneer 65"],
                "soups": ["veg soup5", "veg soup4", "veg soup6"]
            },
            "non_veg":{
                "biryani": ["mutton_dum", "mutton_fry", "mutton_moghali", "mutton_boneless"],
                "starters": ["mutton tikka", "mutton tandoori", "chilli mutton"],
                "soups": ["nonveg soup4", "nonveg soup5", "nonveg soup6"]
            }
        },
        "krana":{
            "veg_items":{
                "biryani": ["green_mushroom", "godaver_kaju", "cow_paneer"],
                "starters": ["potato manchurian", "paneer manchueria", "gobi munchueria"],
                "soups": ["veg soup7", "veg soup8", "veg soup9"]
            },
            "non_veg":{
                "biryani": ["fish_dum", "fish_fry", "fish_moghali", "boneless"],
                "starters": ["fish tikka", "fish_tandoori", "chilli fish"],
                "soups": ["nonveg soup7", "nonveg soup8", "nonveg soup9"]
            }
        },
        "eat_in":{
            "veg_items":{
                "biryani": ["black_mushroom", "gold_kaju_biryeani", "paneer"],
                "starters": ["carrot manchurian", "paneer roast", "gobi 65"],
                "soups": ["veg soup10", "veg soup11", "veg soup12"]
            },
            "non_veg":{
                "biryani": ["dum", "fry", "moghali", "boneless"],
                "starters": ["chicken tikka", "tandoori", "chilli chicken"],
                "soups": ["nonveg soup10", "nonveg soup11", "nonveg soup12"]
            }
        }
        
    }
    
    
print(resturents["navabs"]["non_veg"]["soups"])
print(resturents["vikras"]["veg_items"]["biryani"][1])
print(resturents["krana"]["veg_items"]["starters"])
print(resturents["eat_in"]["non_veg"]["soups"][1])











