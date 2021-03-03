x=int(input("enter the current year: "))
y=int(input("enter the final year: "))
print("leap years:")
while(x<=y):
   if((x%4==0)and((x%100!=0)or(x%400==0))):
               print(x)
               x=x+1
   else:
               x=x+1
