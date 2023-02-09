person = {}
person["fname"] = "Joe"
person["lname"] = "Fonebone"
person["age"] = 51
person["spouse"] = "Edna"
person["children"] = ["Ralph", "Betty", "Joey"]
person["pets"] = {"dog": "Fido", "cat": "Sox"}

#print(person)

#print out the name of the second child
print(type(person['children']))
print(person['children'][1])


# Print out the name of the cat
print(type(person['pets']))
print(person['pets'][3])

# iterate through all children and print out all children

# print out the pets in this format
#       type of pet: dog name of pet: fido


