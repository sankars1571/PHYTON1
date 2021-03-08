def swap(a, b):
       new_a=b[0] + a[1:]
       new_b = a[0] + b[1:]
       print("string:",a+"",b)
       print("After swapping first position:")
       return new_a+" "+ new_b
print(swap('stay', 'home'))
