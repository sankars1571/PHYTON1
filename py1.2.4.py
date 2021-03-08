list1=[6,7,8,9]
list2=[10,11,12,213]
print("list1=",list1)
print("list2=",list2)
if(len(list1)==len(list2)):
                     print("List are in same length")
else:
                     print("List are not in same length")
if(sum(list1)==sum(list2)):
                        print("List sum are equal")
else:
               print("List sum are not equal")
output=any(check in list2 for check in list1)
print("common value: ",output)
