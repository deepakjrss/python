#  mydictionary={
#  
    #  "name":"deepak",
    #  "age":19,
    #  "percent":100
#  }
# mydictionary={
    # "age" : 22
# }
# age=mydictionary.get("age")
# keys=mydictionary.values()
# items=mydictionary.items()
# mydictionary["rollno"]=37
# mydictionary["age"]=33
# a=mydictionary.update({"age":33})
# print(a)
# print(items)
# print(keys)

# print(age)

#ordered
#changable
#doesnot allow duplicate values

dict1={"one":1,"two":2,"three":3}
dict2={"four":4,"five":5,"six":6}
#merge two dictionaries in one

dict1.update(dict2)
print(dict1)