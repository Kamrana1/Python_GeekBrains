def fact(n):
    result=1
    for i in range(1,n+1):
        result*=i
        yield result

f=5
for el in fact(f):
    print(el)
