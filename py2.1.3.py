list=[]
n=int(input("Enter the number of items in the list:" ))
for i in range(0,n):
       list.append(int(input("Enter the element:" )))
print("list=",list)
sum=0
for i in list:
             sum=sum+i
print("sum of all items in the list=",sum)
