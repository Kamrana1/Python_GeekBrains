from random import choice
from itertools import count, cycle

list=[]

for i in count(10):
  list.append(i)
  if i==20:
    break

print(list)

a=0
for i in cycle(list):
  print(i)
  a+=1
  if a==9:
    break