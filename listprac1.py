#list can contain multiple types of data........it is a hetrogeneous type of data collection 
list=["Prem","pagal",420]
list2=["Gymboy","lover boy"]
#append adds to the end of the list
#We can add duplicarte value in the list
#Tuple and list are very similar but tuples are imutable and list are mutable
#mutable=We can make changes to the values in the list
#imutable=We cannot make any changes to the values in a tuple
list[0:1]=["Rohith","Hero"]
print(list[0:2])
print(list)
list.insert(1,"Prem")#insert is used to add an item at a specified position"
print(list)
list.append("Kutte")#Inserts an item at the end of the list
print(list)
list.extend(list2)#Extends the list by adding the given list
print(list)
list.remove("Hero")#Removes the specified item from the list
print(list)
list.pop(-1)#Removes the item at the specified position
print(list)
del list[-1]#Deletes the item at the specified Index
print(list)
list.clear()#Clears the list
print(list)

