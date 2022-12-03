#write a program to unpack the following tuple into four variables and print each variable
#tuple1=(10,20,30,40)


tuple1=("10","20","30","40")
(a,b,c,d)=tuple1
print(a)
print(b)
print(c)
print(d)


tuple1=(10,20)
tuple2=(30,40)
#swap above tuples
#output - tuple1=(30,40)
#tuple2(10,20)

temp=tuple1
tuple1=tuple2
tuple2=temp
print("tuple1=",tuple1)
print("tuple2=",tuple2)


tuple3=(12,24)
tuple4=(16,32)
tuple3,tuple4=tuple4,tuple3
print(tuple3)
print(tuple4)


tuple1=(1,[6,7],2,3,4,5)
list1=list(tuple1)
list1[1][0]=8
tuple1=tuple(list1)
print(tuple1)

