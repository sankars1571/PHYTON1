y={'alex':4,'milan':2,'kas':1,'ram':3}
l=list(y.items())
l.sort()
print("Ascending order: ",l)
l=list(y.items())
l.sort(reverse=True)
print("Descending order: ",l)
dict=dict(l)
print("Dictionary:",dict)
