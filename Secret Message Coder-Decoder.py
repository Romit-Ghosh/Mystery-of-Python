# Write a python program to translate a message into secret code language. Use the rules below to translate normal English into secret code language

# Coding:
# if the word contains atleast 3 characters, remove the first letter and append it at the end
#   now append three random characters at the starting and the end
# else:
#   simply reverse the string

# Decoding:
# if the word contains less than 3 characters, reverse it
# else:
#   remove 3 random characters from start and end. Now remove the last letter and append it to the beginning
# Your program should ask whether you want to code or decode

import random
import string

def generate_random_string(length):
  return ''.join(random.choice(string.ascii_lowercase) for i in range(length))

st = input("Enter message : ")
words = st.split(" ")
coding = input("1 for Coding or 0 for Decoding :  ")
coding = True if (coding=="1") else False
#print(coding)
if(coding):
  nwords = []
  for word in words:
    if(len(word)>=3):
      random_chars1 = generate_random_string(3)
      random_chars2 = generate_random_string(3)
      stnew = random_chars1+ word[1:] + word[0] + random_chars2
      nwords.append(stnew)
    else:
      nwords.append(word[::-1])
  print(" ".join(nwords))

else:
  nwords = []
  for word in words:
    if(len(word)>=3):
      stnew = word[3:-3]
      stnew = stnew[-1] + stnew[:-1]
      nwords.append(stnew)
    else:
      nwords.append(word[::-1])
  print(" ".join(nwords))

