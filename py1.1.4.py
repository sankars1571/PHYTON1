new =input("enterr the word;")
vowels=['a','e','i','o','u']
list1=[]
for x in new:
              if (x in vowels and x not in list1):
                                                  list1.append(x)
print("Vowels present in given word:",list1)
