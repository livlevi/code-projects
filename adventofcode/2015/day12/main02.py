import json

sumjson = 0
#Recursive function that interates through each object.
#Checks the type of the object and operates on it based on type

def sumitems(item):
    if type(item) is int:
        return item
    # If the item is an integer, return it so it can be added to the sum
    if type(item) is list:
        return sum(map(sumitems, item))
    # If list, then map the function to each item
    if type(item) is dict:
        things = item.values()

        if "red" in things:
            return 0
        # No need to add the value if it has red
        return sum((map(sumitems, things)))
    
    else:
        return 0
    
with open("input.json") as file:
    obj = json.loads(file.read())
    sumjson += sumitems(obj)
    print(sumjson)