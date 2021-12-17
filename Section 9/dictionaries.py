programming_dictionary = {
 "Bug": "An error in a program that prevents the program from running as expected.",
 "Function": "A piece of code that you can easily call over and over again.",
}
#Retrieving items from disctionary
# print(programming_dictionary["Bug"])

# #Adding new items to dictionary
# programming_dictionary["Loop"] = "The action of doing something over and over again"
# print(programming_dictionary["Loop"])

#Crate a new dictionary
empty_dictionary = {}

# #Wipe an existing disctionary
# programming_dictionary = {}
# print(programming_dictionary)

#Edit items to dictionary
# programming_dictionary["Bug"] = "edited"
# print(programming_dictionary["Bug"])

#Loop through a dictionary
# for key in programming_dictionary:
#     print(key)
#     print(programming_dictionary[key])


#NEsting
capitals = {
    "France: Paris",
    "Germany":"Berlin",
}
#Nesting a list in dictionary
tavel_log ={
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Berlin", "Frankfurt", "Hamburg"],
}

#Nesting dictionary in a Dictionary
tavel_log ={
    "France": {"cities_visited": ["Paris", "Lille", "Dijon"],
              "total_visists": 12,
               },
    "Germany": {"cities_visited":["Berlin", "Frankfurt", "Hamburg"],
                "total_visists": 5,},
}

#NEsting a dictionary in a List

tavel_log = {
    {"country": "France",
     "cities_visited": ["Paris", "Lille", "Dijon"],
     "total_visists": 12,
     },
    {"country":"Germany",
     "cities_visited":["Berlin", "Frankfurt", "Hamburg"],
     "total_visists": 5,
     },
}

