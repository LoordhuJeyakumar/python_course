#Dictionary

#dictionary syntex

dictionary_syntex = {"key1": "value1", "key2": "value2", "key3": "value3"}
print(dictionary_syntex)

empty_dictionary = {}   
print(empty_dictionary)
print(type(empty_dictionary))

#class constructor

dictionary = dict()
print(dictionary)
print(type(dictionary))

pairs = [("apple", 1), ("banana", 2), ("cherry", 3)]
fruit_dict = dict(pairs)
print(fruit_dict) # Output: {'apple': 1, 'banana': 2, 'cherry': 3}

#Accessing values

fruit_dict = {"apple": 1, "banana": 2, "cherry": 3}
print(fruit_dict["apple"]) # Output: 1
print(fruit_dict["banana"]) # Output: 2
print(fruit_dict["cherry"]) # Output: 3
print(fruit_dict.get("apple")) # Output: 1
print(fruit_dict.get("banana")) # Output: 2
print(fruit_dict.get("cherry")) # Output: 3
print(fruit_dict.get("date")) # Output: None
print(fruit_dict.get("date","Not found")) # Output: Not found
print(fruit_dict.get("date", 0)) # Output: 0
print(fruit_dict.get("date", None)) # Output: None
print(fruit_dict.get("date", False)) # Output: False

#handling errors

fruit_dict = {"apple": 1, "banana": 2, "cherry": 3}
if "apple2" in fruit_dict:
    print(fruit_dict["apple"]) # Output: 1
else:
    print("Key not found")

print(fruit_dict["apple"])


#dictionary mutability

fruit_dict = {"apple": 1, "banana": 2, "cherry": 3}

fruit_dict["apple"] = 4
print(fruit_dict) # Output: {'apple': 4, 'banana': 2, 'cherry': 3}
fruit_dict["date"] = 5
print(fruit_dict) # Output: {'apple': 4, 'banana': 2, 'cherry': 3, 'date': 5}
fruit_dict["apple"] = 6
print(fruit_dict) # Output: {'apple': 6, 'banana': 2, 'cherry': 3, 'date': 5}

fruit_dict["apple"] = fruit_dict["apple"] + 1
print(fruit_dict) # Output: {'apple': 7, 'banana': 2, 'cherry': 3, 'date': 5}


#removing items

fruit_dict = {"apple": 1, "banana": 2, "cherry": 3}
del fruit_dict["apple"]
print(fruit_dict) # Output: {'banana': 2, 'cherry': 3}
removed = fruit_dict.pop("banana","none")
print(removed) # Output: none


items_dict = {"item1": 100, "item2": 200, "item3": 300}
removed_item_pair = items_dict.popitem() # Removes and returns last inserted pair (e.g., might remove ('item3', 300))
print(items_dict) # Output: (e.g.) {'item1': 100, 'item2': 200}
print(removed_item_pair) # Output: (e.g.) ('item3', 300)
# empty_dict = {}
#empty_dict.popitem() # KeyError: 'popitem(): dictionary is empty'


#dictionary methods

fruit_dict = {"apple": 1, "banana": 2, "cherry": 3}
print(fruit_dict.keys()) # Output: dict_keys(['apple', 'banana', 'cherry'])
print(type(fruit_dict.keys()))
 # Output: <class 'dict_keys'>
print(list(fruit_dict.keys())) # Output: ['apple', 'banana', 'cherry']

print(fruit_dict.values()) # Output: dict_values([1, 2, 3])
print(type(fruit_dict.values()))
 # Output: <class 'dict_values'>
print(list(fruit_dict.values())) # Output: [1, 2, 3]

print(fruit_dict.items()) # Output: dict_items([('apple', 1), ('banana', 2), ('cherry', 3)])


dict1 = {"a": 1, "b": 2, "c": 3}
dict2 = {"c": 30, "d": 4, "e": 5} # 'c' is a common key, 'd' and 'e' are new keys

dict1.update(dict2) # Update dict1 with key-value pairs from dict2
print(dict1) # Output: {'a': 1, 'b': 2, 'c': 30, 'd': 4, 'e': 5} # Value for 'c' is updated, new keys 'd', 'e' added

dict1 = {"a": 1, "b": 2, "c": 3}
dict2 = {"c": 30, "d": 4, "e": 5} # 'c' is a common key, 'd' and 'e' are new keys

dict2.update(dict1) # Update dict2 with key-value pairs from dict1
print(dict2) # Output: {'c': 1, 'd': 2, 'e': 3, 'a': 30, 'b': 4, 'c': 5} # Value for 'c' is updated, new keys 'a', 'b', 'c' added

#copying dictionaries

fruit_dict = {"apple": 1, "banana": 2, "cherry": 3}
fruit_dict_copy = fruit_dict.copy()
print(fruit_dict_copy) # Output: {'apple': 1, 'banana': 2, 'cherry': 3}
fruit_dict_copy["apple"] = 4
print(fruit_dict_copy) # Output: {'apple': 4, 'banana': 2, 'cherry': 3}


#dictionary iteration

fruit_dict = {"apple": 1, "banana": 2, "cherry": 3}
for key in fruit_dict:
    print(key) # Output: apple banana cherry
    print(fruit_dict[key]) # Output: 1 2 3
    print(key, fruit_dict[key]) # Output: apple 1 banana 2 cherry 3


#dictionary comprehension 

fruit_dict = {"apple": 1, "banana": 2, "cherry": 3}
fruit_dict = {key: value * 2 for key, value in fruit_dict.items()}
print(fruit_dict) # Output: {'apple': 2, 'banana': 4, 'cherry': 6}

#nested dictionaries

fruit_dict = {"apple": 1, "banana": 2, "cherry": 3}
nested_dict = {"fruit": fruit_dict, "vegetable": {"carrot": 4, "potato": 5}}
print(nested_dict) # Output: {'fruit': {'apple': 1, 'banana': 2, 'cherry': 3}, 'vegetable': {'carrot': 4, 'potato': 5}}