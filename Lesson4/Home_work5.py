from functools import reduce
data=[]

for elem in range(100,1001):
    if elem%2==0:
        data.append(elem)

sumreduce= reduce(lambda elem1, elem2: elem1+elem2,data)
print(f"Reduce result: {sumreduce}")