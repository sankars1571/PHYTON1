string=input("Enter name;")
word=list(string)
ch=string[0]
length=len(v)
for i in range(1,length):
               if(word[i]==ch):
                              word[i]='$'
print(word)
