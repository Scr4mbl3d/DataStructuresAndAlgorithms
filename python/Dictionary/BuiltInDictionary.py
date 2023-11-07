# ========================================
#     File name: BuiltInDictionary.py
#     Author: Aadhawan Maadheshwaran
#     Date created: 11/07/2023
#     Date last modified: 11/07/2023
#     Python Version: 3.12.0
# ========================================

dic = {'Name':'Scrambled',
       'Age': 23,
       'Comment': 'Good Boy',
       'isCrazy': True}


#access
print(dic)
print("\n---------------------")
print("- Access Operations -")
print("---------------------")
print("Accessing value by key:  ", dic["Name"])
print("Accesing value by get:   ", dic.get('year'))
print("Accesing keys:           ", list(dic.keys()))
print("Accesing Value:          ", list(dic.values()))
print("Accessing key value pair:", list(dic.items()))
#Dictionaries cannot have two items with the same key

#insert
print("\n---------------------")
print("- Insert Operations -")
print("---------------------")
dic['gpa'] = 3
print("Inserting a pair: ", dic)
dic['Age'] = 20
print("replacing a value:", dic)

#search
print("\n---------------------")
print("- Search Operations -")
print("---------------------")
print("Reference of the dict:    ", dic)
print("In operator (key in dict):  ", 'Name' in dic)
print("In operator (value in dict):  ", 21 in list(dic.values()))

#delete
print("\n---------------------")
print("- Delete Operations -")
print("---------------------")
print("Reference of the list:  ", dic)
del(dic['gpa']) #removes the value in the index
print("Deleting by key:        ", dic)
popped = dic.pop('Age') #index should be given
print("Deleting by pop method: ", dic)
print("Popped number from list:", str(popped))
popped = dic.popitem() #pop the last added pair in the dict as a tuple
print("Deleting by pop method: ", dic)
print("Popped number from list:", str(popped))

# -- Result --

# {'Name': 'Scrambled', 'Age': 23, 'Comment': 'Good Boy', 'isCrazy': True}

# ---------------------
# - Access Operations -
# ---------------------
# Accessing value by key:   Scrambled
# Accesing value by get:    None
# Accesing keys:            ['Name', 'Age', 'Comment', 'isCrazy']
# Accesing Value:           ['Scrambled', 23, 'Good Boy', True]
# Accessing key value pair: [('Name', 'Scrambled'), ('Age', 23), ('Comment', 'Good Boy'), ('isCrazy', True)]

# ---------------------
# - Insert Operations -
# ---------------------
# Inserting a pair:  {'Name': 'Scrambled', 'Age': 23, 'Comment': 'Good Boy', 'isCrazy': True, 'gpa': 3}
# replacing a value: {'Name': 'Scrambled', 'Age': 20, 'Comment': 'Good Boy', 'isCrazy': True, 'gpa': 3}

# ---------------------
# - Search Operations -
# ---------------------
# Reference of the dict:     {'Name': 'Scrambled', 'Age': 20, 'Comment': 'Good Boy', 'isCrazy': True, 'gpa': 3}
# In operator (key in dict):   True
# In operator (value in dict):   False

# ---------------------
# - Delete Operations -
# ---------------------
# Reference of the list:   {'Name': 'Scrambled', 'Age': 20, 'Comment': 'Good Boy', 'isCrazy': True, 'gpa': 3}
# Deleting by key:         {'Name': 'Scrambled', 'Age': 20, 'Comment': 'Good Boy', 'isCrazy': True}
# Deleting by pop method:  {'Name': 'Scrambled', 'Comment': 'Good Boy', 'isCrazy': True}
# Popped number from list: 20
# Deleting by pop method:  {'Name': 'Scrambled', 'Comment': 'Good Boy'}
# Popped number from list: ('isCrazy', True)