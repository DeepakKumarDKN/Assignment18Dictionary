"""1. Write a python program to create and print a dictionary which stores your information.
(name, age, gender .....)"""

# dictOne = dict(name="deepak",age=22,gender="Male")
# print(dictOne)

"""2. Write a python program to access the items of a dictionary by referring to its key
name."""

# dictOne = dict(name="deepak",age=22,gender="Male")
# for keys in dictOne:
#   print(dictOne[keys])


"""3. Write a python program to get a list of the values from a dictionary."""


# dictOne = dict(name="deepak",age=22,gender="Male",course="Fullstack Development Python",mentor='MysirG')
# for values in dictOne.values():
#   print(values)

"""4. Write a python program to change the value of a specific item by referring to its key
name."""

# dictOne = dict(name="deepak",age=22,gender="Male",course="Fullstack Development Python",mentor='MysirG')
# for k,v in dictOne.items():
#   if k == "name":
#     dictOne[k] = "Deepak"
#   else:
#     pass

# print(dictOne)


"""5. Write a python program to print all key names in the dictionary, one by one."""

# dictOne = dict(name="deepak",age=22,gender="Male",course="Fullstack Development Python",mentor='MysirG')
# for keys in dictOne.keys():
#   print(keys)

"""6. Write a python program to create a dictionary that contains three dictionaries.
(nested)"""
# dictone = {'dict1':{'name':'deepak','age':22},
#            'dict2':{'name':'Rahul', 'age':23},
#            'dict3':{'name':'Dhoni','age':'dontKnow'}}
# print(dictone)

"""7. Write a python program to create three dictionaries, then create one dictionary that
will contain the other three dictionaries."""





"""8. Write a python program to convert two lists into a dictionary in a way that item from
list1 is the key and item from list2 is the value."""

# Listone = [10,20,30,40]
# listTwo = ['deepak','rahul','divyansh','devika']

# finalDic = {k:v for(k,v) in zip(Listone,listTwo)}
# print(finalDic)

"""9. Write a python program to merge two python dictionaries into one dictionary."""

# dictOne = dict(name="deepak",age=22,gender="Male",course="Fullstack Development Python",mentor='MysirG')
# dictTwo = dict(fees=4000, instituteName= 'Ineuron' )
# dictOne.update(dictTwo)
# print(dictOne)

"""10. Write a python program to get the key of lowest value from the dictionary.
sample_dict = {
'C': 92,
'Java': 66,
'Python': 85
}"""


# sample_dict = {'C': 92,'Java': 66,'Python': 85}
# minValue = sample_dict["C"]
# for k,v in sample_dict.items():
#   if v <= minValue:
#     minValue = v
# for k,v in sample_dict.items():
#   if v == minValue:
#     print(k)
#     break



