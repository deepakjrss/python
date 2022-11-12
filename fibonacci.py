a=0
b=1

for i in range(0,10):
    sum=a+b
    a=b
    b=sum
    i=i+1
    print(sum,end=" ")
    
