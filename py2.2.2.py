def find_longest_word(words_list):
         word_len=[]
  for n in words_list:
     word_len.append((len(n), n))
  word_len.sort()
  return word_len[-1][0], word_len[-1][1]
words_list=[]
for i in range(0,4):
   words_list.append(input("Enter a word:"))
print(words_list)
result=find_longest_word(words_list)
print("\nLongest word: ",result[1])
print("Length of the longest word: ",result[0])
