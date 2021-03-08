d1 = {'India':5,'Canada':6,'Japan':2}
d2 = {'France':1,'Malaysia':3}
d3 = d1.copy()
for key, value in d2.items():
     d3[key] = value
print("d1=",d1)
print("d2=",d2)
print("After Merging:",d3)
